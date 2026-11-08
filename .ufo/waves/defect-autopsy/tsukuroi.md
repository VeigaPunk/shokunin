# tsukuroi defect autopsy — rounds 88–90 rejected-honest-stop

Lane: tsukuroi (OS/boot). Admitted 85, 86, 87; rejected 88, 89, 90.
Read-only autopsy. Sources pinned to file:line as observed at write time (2026-11-07).

## Admitted baseline 85–87 (for contrast)

- r85 C2 (hibernate-availability gate v2, battery 20/20 ×3): discrimination partial, lane-reported (M3/M4, QUALITY 122); spot-check admits because candidate itself conforms clause-by-clause and no candidate-free forger reaches target. `tsukuroi-shokunin/corpus/lessons/round-85-verifier-spotcheck.md:51-57`.
- r86 C1 (kernel parse, battery 30/30 ×3): same shape — CriticClaims f4-shortcut reads 30/30, lane reports M2/R86-R3, spot-check admits. `tsukuroi-shokunin/corpus/lessons/round-86-verifier-spotcheck.md:53-58`.
- r87 C1 (limine pin gate v1, battery 22/22 ×3): 10 R1–R7 clauses uncertified (g01–g08,g10,g14 read 22/22), lane reports M3/QUALITY 125, spot-check admits. `tsukuroi-shokunin/corpus/lessons/round-87-verifier-spotcheck.md:52-56`.

The admitted class: a direct behavioural battery whose target the candidate meets, with a named, quantified calibration gap disclosed but not blocking the declared predicate. Key mechanism (all three): instrument gap against *other* gates, candidate verified by direct code read.

## What changed at 88

The surface moved to meta-instrument (a counter judging a battery) and then, after two folds of the same fold, back to the gate surface with a fidelity defect. See per-round below and §Contrast.

---

## Round 88 — 3/3, 45/45 ×3, NOT VERIFIED (isolation + determinism)

### 1. Rejection reason, verbatim (closure)

MANIFEST `notes` (MANIFEST.json:55184) and `verification.rechecks` (MANIFEST.json:55179).

`verification.rechecks` excerpt (full string at MANIFEST.json:55179, truncated in read output only):
> "NOT VERIFIED as declared: freeze roster-oracle control unmet only by crash (48 FileNotFoundError rows), same control met 3/3 45/45 from clone layout …"

`notes` excerpt (MANIFEST.json:55184):
> "honest stop - C1 (measured, operability 9 assurance arm) reached 3/3 45/45 x3 on the frozen counter but its predicate's isolation clause is falsified by the lane's own wave (roster-oracle control passed only by crash at freeze, met from the clone layout the declared measurements used) and two negatives are killed by chance (CRLF); the L1 itself reports C1 not verified as a forgery-resistant measurement; operability unchanged."

Verdict lines: MANIFEST.json:55159-55160 `"admitted": false, "verdict": "rejected-honest-stop"`.

Spot-check ruling (tsukuroi-shokunin/corpus/lessons/round-88-verifier-spotcheck.md:55-60):
> "Ruling: the 45/45 ×3 numbers verify, but the claim's predicate includes an isolation property its own forgery control falsifies in the layout the declared measurements used, and a three-run kill the battery meets only by chance on `N-m22`/`N-g15`. The L1 states the same ("not verified as a forgery-resistant measurement"). C1 does not verify as declared → operability **unchanged** (r84 precedent: a lane-disclosed falsified instrument is an honest stop)."

### 2. Claim vs measured

- Claim (frozen at SCORECARD.md:7414, truncated line `7414:7414` — see raw): battery under counter over 48-gate roster reads met for 3 POSITIVE, unmet for 45 NEGATIVE ×3, "with every gate handed to the battery as a freshly renamed, nonce-perturbed copy inside a sandbox that hides the lane repository". Target 3/3 and 45/45 ×3.
- Measured: 3/3, 45/45 in each of three runs at 5b98ca98 and 1fac4195, both layouts. Lane report §Before→after: ".ufo/reports/round-88/tsukuroi.md:107-113" — target met by frozen counter; **not verified as a forgery-resistant measurement** (wave falsified counter isolation after scoring F1–F3).
- Non-author re-run disagreement: post-freeze clone-layout re-run of the roster-oracle control reads `3/3, 45/45 verdict met rc=0` (tsukuroi-shokunin/.ufo/waves/round-88/after/controls-clone-layout.txt, roster-oracle block), vs freeze receipt 0/3, 0/45 ×3 (tsukuroi-shokunin/.ufo/waves/round-88/before/controls/controls-summary.txt:21-24, bat-roster-oracle rows). Freeze "unmet" was a crash: `bat-roster-oracle.json:67` `FileNotFoundError … roster-r88.json` inside sandbox.

C2 (entry PW1–PW9) was ruled `unprovable-but-better` by the closure (spot-check:62). The rejection is C1-only.

### 3. Instrument green? Class?

Instruments ran green on the frozen counter but the green does not survive closure.

- **Class (a) green but unprovable wording/scope**: primary. The predicate asserts isolation ("sandbox that hides the lane repository") as part of the claim; the counter's bwrap sandbox masks only the invoking copy, so isolation fails in the clone layout. The declaration's own caveat ("Not certified: … battery that recognises roster gates by behaviour-preserving normalisation", SCORECARD.md:7422-7424) was narrowed by the non-author to "the verdict path never reads the roster" (spot-check:50-53) — the battery itself is behavioural, but the counter's isolation clause is false.
- **Class (c) before/after did not re-derive** (secondary): two negatives killed by chance. `WHITESPACE-CRLF` draws CRLF p 0.6/case; N-m22/N-g15 escape a run with p ≈ 2.6%. The three-run kill holds by chance on two gates (spot-check:46-49; w1/MutBattery.md §3–4 as cited at spot-check:46; L1 report :63-66).
- Not (b) never green: 45/45 ×3 reproduced independently by ExecReplicate (L1 report :43-44, :37-39). Not (d): non-author did not execute (Gate standard) — disagreement is committed-evidence re-run from clone, not a fresh execute. Not (e): the lane could see the isolation defect (CriticClaims F1–F3) and did.

---

## Round 89 — 3/3, 62/62 ×3, NOT VERIFIED (name channel oracle)

### 1. Rejection reason, verbatim (closure)

MANIFEST `notes` (MANIFEST.json:55591):
> "Honest stop: the lane's wave falsified its own frozen counter (gate run under roster file name; argparse usage leak) and the L1 filed C1 as not verified."

`verification.rechecks` tail (MANIFEST.json:55586):
> "usage-oracle on frozen counter 3/3 62/62 x3 with 65/65 name hits per run; counter line 211 copies gate under roster basename vs docstring line 24 -> instrument falsified, C1 NOT VERIFIED, operability unchanged."

Spot-check ruling (tsukuroi-shokunin/corpus/lessons/round-89-verifier-spotcheck.md:51-56):
> "Ruling: the 62/62 ×3 numbers verify, but the claim's predicate includes "the battery sees each gate only as an opaque launcher", and a battery that tests no rule meets the same target on the frozen counter. The frozen instrument cannot separate the candidate from a forgery, so C1 does not verify as declared → operability **unchanged** (no ordinal move was claimed; r84/r88 precedent: a lane-disclosed falsified instrument is an honest stop)."

### 2. Claim vs measured

- Claim (SCORECARD.md:7491): battery reads met for 3 POSITIVE, unmet for 62 NEGATIVE with zero error rows ×3; "the battery sees each gate only as an opaque launcher that forwards its argv to the gate run outside the battery's sandbox".
- Counter docstring (tools/battery-discrimination-r89.py line 24, cited at spot-check:44-45): "No source text, digest or file name of a roster gate is visible to the battery".
- Measured: 3/3, 62/62, 0 errors ×3 (9 runs incl. canonical + clone, spot-check:37-38). Matches report.
- Forgery: `usage-oracle.py` (name→label table, evaluates no rule) reads 3/3, 62/62, verdict met rc 0 ×3 on frozen counter, 65 hits/run (tsukuroi-shokunin/.ufo/waves/round-89/after/forgeries/usage-oracle.receipt.txt:4-13; spot-check:47-49). Counter line 211 (`os.path.join(gd, os.path.basename(gate["abs"]))`, spot-check:45-47) runs gate under roster file name; argparse usage text leaks it back.

L1 falsified as instrument and filed NOT VERIFIED (L1 report :46-50, lesson M3/QUALITY 129).

C2 (entry UF1–UF8) ruled `unprovable-but-better` (spot-check:79-83). Rejection is C1-only.

### 3. Instrument green? Class?

Green on frozen counter, does not survive.

- **Class (a) green but unprovable wording/scope**: primary. The header predicate "opaque launcher / no file name visible" is not an instrument property the counter enforces; a name-table oracle meets the target. Same shape as r88 F1–F3, new channel (argv/usage text rather than filesystem visibility).
- **Class (d) non-author re-run disagreed** in the evidence sense: CriticClaims' patched counter (constant name `gate.py`) reads candidate 62/62 but oracle unmet (spot-check:54-56) — the isolation holds only with the patch, proving the frozen instrument is the defect. (The non-author did not execute; CriticClaims is a wave seat = the lane, and the closure re-verified from committed JSON.)
- Not (b): 62/62 ×3 green. Not (c): before/after re-derived; do-nothing 46/45-46 etc. verified. Not (e): lane found and proved it with the usage oracle before closure.

---

## Round 90 — 73/73 ×3, NOT VERIFIED (rule-set fidelity)

### 1. Rejection reason, verbatim (closure)

MANIFEST `notes` (MANIFEST.json:55912):
> "Honest stop (third in a row): wave seat ReviewSource F1 showed Limine reads measured_boot/hash_mismatch_panic from the global section only (config.c 642-650); the frozen r90 battery and r87 R6 encode whole-file visibility, so 73/73 certifies Limine-false answers; the L1 filed C1 NOT VERIFIED."

Spot-check ruling (tsukuroi-shokunin/corpus/lessons/round-90-verifier-spotcheck.md:54-58):
> "**C1: NOT VERIFIED** — the frozen predicate certifies Limine-false answers; the lane filed it so. Axis grade: **operability unchanged** … the wrong `on_panic` arises only for `measured_boot` inside an entry body, a shape absent on this host (`after/live-receipt.txt`: `measured_boot None`, `on_panic menu`, `/boot` digest list identical before/after) … Routed R90-R1 below."

### 2. Claim vs measured

- Claim (SCORECARD.md:7567): gate follows Limine v12.9.4 rule set R1–R7,R9–R10 + R8: 73/73 families met ×3, canonical + clone.
- Measured: 73/73 ×3 both layouts (L1 report :38-40, :68-72; spot-check:39-44). Controls K1 0/0/0 & 1/0/0, K2 51/50/51 & 51/51/50, N21–N27 killed 3/3 by named families.
- Fidelity defect: ReviewSource F1, re-read by L1 at config.c raw 642–650 (L1 report :41-44): Limine reads `hash_mismatch_panic`/`measured_boot` only from global section unless line 1 is an entry; r90 R10 and r87 R6 say "whole file". Families MEASURED-IN-ENTRY and PANIC-AFTER-PIN certify Limine-false answers. Control N21 (Limine-true global-only reading) is killed 3/3 by MEASURED-IN-ENTRY (spot-check:50-52).
- Probe: `after/visibility-probe.txt` shows landed gate answering `on_panic halt` for case A (measured in entry with header) where global-only gate answers `menu` (tsukuroi-shokunin/.ufo/waves/round-90/after/visibility-probe.txt:2-6, cases A–D; spot-check:52-54).

C2 (entry TV1–TV9) ruled `unprovable-but-better` (spot-check:82-87). Rejection is C1-only.

### 3. Instrument green? Class?

Green (73/73 ×3), does not survive.

- **Class (a) green but unprovable wording/scope**: primary root cause, with a fidelity twist. The battery certifies a predicate ("follows the rule set") that misstates source behaviour; the green is therefore unprovable-as-worded. This is the same r85-r87 calibration-gap shape but promoted to blocking: the gap is not a breadth shortfall (uncertified clauses) but a wrong clause (whole-file visibility) contradicted by the pinned source.
- **Class (e) structural defect nothing in the lane could see** — no: the lane's ReviewSource seat found it, and the L1 re-read config.c 642–650 and built the visibility probe before closure. It is a lane-visible defect that survived because the declaration froze the wrong visibility rule (QUALITY 131, SCORECARD.md:7602-7604).
- Secondary uncredited channels noted post-hoc (CriticClaims §1 oracle-reuse reads 73/73, SCORECARD.md:7594-7596) are the r88/r89 name-channel class reappearing in a new channel, but the closure's blocking reason is fidelity (R90-R1), not the oracle channel.

---

## The objcopy host-state question (round-86 incident → 88–90)

### Facts

- Round-86 seat ScoutHost ran `sudo objcopy --dump-section` on `/boot/EFI/Linux/*.efi`; objcopy (no outfile operand) rewrote both UKIs in place (L1 report round-86 :139-143). Damage: 5 PE header bytes each, payloads unchanged (same lines).
- After-state (read-only re-checks): `/boot/limine.conf:30` pins `b990d8c6…`, `:38` pins `a68c281d…`; disk `b2sum` is `57f5eb94…` / `eff78d32…` (round-86 spot-check:120; round-87 spot-check:50; round-88 L1 report :171-172 noting pins still mismatch).
- Live verification at autopsy time (read-only, sudo -n, 2026-11-07): disk `b2sum` `/boot/EFI/Linux/omarchy_linux.efi` = `57f5eb9420f462c798a9e7dbf01f9fadbe12332c595f48e199d86f9ab039078ab0f65d2bf52c60a5a0a905003b27c3cece4cfddcea612c4f6f2d164fffcdb5b1`, `omarchy_linux-lts.efi` = `eff78d32b1aed09d6b48e584e6ab88c5a9062fa4ed57d98bd6553e8efbf09928425eecbd451ee7b2f3bcabe0b7c9b34e777125470fc8ae5eb33a8cdda27ed4e5`, while `/boot/limine.conf` lines 30/38 still pin `b990d8c6…` / `a68c281d…`. Host is still in the post-incident mismatched state.
- The gate's live verdict on this host is `LP-MISMATCH` rc 1, consequence `prompt` (not panic) on lines 30/38 (round-87 L1 :49-51; round-90 L1 :38-40; spot-checks record the same).

### Causation verdict: NO — the host-state change did not poison 88–90.

Evidence:

1. The poisoned host state is exactly what the r87 gate was built to *detect*, and it does detect it: `--live` rc 1 LP-MISMATCH prompt on lines 30/38, with `/boot` digest list identical before/after each live run (round-87 spot-check:50; round-90 spot-check:55-58). A boot-integrity gate that "can no longer pass" is not what blocked 88–90: no 88–90 claim predicates on host live HEALTHY. The C1 counters measure battery calibration on synthetic fixtures, not the live host.
2. The 88–90 blocking defects are host-independent: r88 roster visibility in the clone layout (bwrap binds `/`, masks only the invoking copy), r89 argv/usage name leak (counter line 211), r90 config.c 642–650 visibility rule. Each is falsified on pinned tool bytes / upstream source, not on `/boot` state. The host mismatch even confirms the gate works (rc 1 prompt, not panic), as the spot-checks state.
3. Round-87 itself — the first round to gate the Limine pin plane — was admitted with the host already poisoned (pins mismatched at r87 closure, spot-check:15-16 "still present and stays operator-owned"). If host state poisoned the gate, r87 would have failed; it did not.

[INFERENCE] The objcopy incident shaped *motivation* (it created the Limine pin plane as a topic and the r86 routed defect), but not the *mechanism* of 88–90 rejection. The incident is a counterexample, not a cause.

---

## 85–87 vs 88–90 contrast — what changed at 88, concretely

Three concrete changes, in order of blocking weight:

1. **Claim surface: direct gate → meta-instrument (counter judging a battery).** In 85–87 C1 predicates read "gate X reaches N/N on battery Y (target N/N", with the candidate itself code-reviewable and the battery a direct behavioural probe. At 88 the predicate became "battery reads met/unmet over a 48-gate roster *inside a sandbox that hides the lane repository*" (SCORECARD.md:7414). The counter added a second trust layer (isolation, nonce-perturbation, rename) whose properties are part of the claim but not enforced by any pre-freeze control *in the measurement layout* (clone). The r88 controls were run canonical at freeze; the declared measurements ran from a clone (L1 report :73-77 post-freeze clone re-run). The isolation property holds in one layout and fails in the other — a layout-dependent predicate. In 89 the counter rebuilt isolation (allowlist sandbox, opaque launcher) and immediately leaked through a new, uncontrolled channel (argv/usage text via roster file name, counter :211 vs docstring :24). Meta-instruments have more channels than any one freeze enumerates; the lane chased its own counter twice and was falsified both times.
2. **Gate: freeze-time forgery controls vs post-freeze falsification.** In 85–87 forgery controls (K0–K6, K1 do-nothing, near-misses) were committed at freeze and held at tip; the calibration gap was disclosed as a limit (QUALITY 122/125) and did not contradict the predicate. At 88–89 the freeze-time forgery control (roster oracle; name oracle) passed by crash or was never tried, and the *same* control met the target when re-run in the measurement layout. The wave falsified the instrument after scoring; the L1 correctly refused to read the green as proof. The protocol's honest-stop rule then forces rejection.
3. **At 90, surface back to gate, but fidelity gate added.** The lane abandoned the counter (SCORECARD.md:7542-7543 "no counter is used") and claimed gate rule-set fidelity (R1–R7,R9–R10) as the operability measure. That moved the blocking class from counter channels to source fidelity: the frozen predicate now certifies answers that contradict config.c 642–650. The defect was latent since r87 R6 (whole-file visibility) but only became blocking when R10 made it load-bearing and the battery encoded it as a family (MEASURED-IN-ENTRY). Gate-surface claims inherit the lane's full source-reading debt; a wrong rule in the battery certifies false gate answers with a green count.

Host state is not in the list: identical mismatched host throughout 87–90; r87 admitted on it.

---

## Dominant mechanism

Three rejected rounds, one mechanism family with two sub-channels, plus a fidelity tail.

**One-sentence mechanism:** In 88–90 the lane froze predicates (counter isolation / opaque-launcher / rule-set fidelity) whose *stated* properties were wider than the *frozen instrument* could enforce, scored green on the frozen instrument, and the closure rejected because the lane's own wave then produced a committed counterexample (roster oracle met from clone; name oracle 62/62; visibility probe halt-vs-menu) proving the predicate unprovable-as-worded.

### Class counts (primary class per round; secondary in parentheses)

| Class | R88 | R89 | R90 | Total |
|---|---|---|---|---|
| (a) green but unprovable wording/scope | ✓ | ✓ | ✓ | 3 |
| (b) never green | — | — | — | 0 |
| (c) before/after did not re-derive | (✓ CRLF chance) | — | — | 1 |
| (d) non-author re-run disagreed | (✓ clone oracle) | (✓ patched counter) | — | 2 |
| (e) structural, lane-blind | — | — | — | 0 |

Secondary counts are the same counterexample seen from the verifier side: the non-author re-ran the forgery control in the measurement layout / patched counter and got the opposite verdict.

### Three strongest verbatim quotes

1. r88 spot-check ruling (tsukuroi-shokunin/corpus/lessons/round-88-verifier-spotcheck.md:55-57, full sentences at :55-60):
> "Ruling: the 45/45 ×3 numbers verify, but the claim's predicate includes an isolation property its own forgery control falsifies in the layout the declared measurements used, and a three-run kill the battery meets only by chance on `N-m22`/`N-g15`."

2. r89 spot-check ruling (tsukuroi-shokunin/corpus/lessons/round-89-verifier-spotcheck.md:51-53):
> "Ruling: the 62/62 ×3 numbers verify, but the claim's predicate includes "the battery sees each gate only as an opaque launcher", and a battery that tests no rule meets the same target on the frozen counter."

3. r90 spot-check ruling (tsukuroi-shokunin/corpus/lessons/round-90-verifier-spotcheck.md:54-55):
> "**C1: NOT VERIFIED** — the frozen predicate certifies Limine-false answers; the lane filed it so."

### Objcopy host-state causation

**No.** See section above. Host still mismatched (`57f5eb94…`/`eff78d32…` on disk vs `b990d8c6…`/`a68c281d…` pins, `/boot/limine.conf:30,38`), gate correctly reads rc 1 LP-MISMATCH prompt on it, r87 was admitted on the same host state, and all three blocking defects are host-independent instrument/fidelity falsifications on pinned bytes.

### Could a lane-side pre-file gate have caught it BEFORE filing?

**Yes — in all three rounds.** The lane already collects the evidence; it needs a pre-file check that *forbids filing a green as verified when the committed counterexample exists in the wave record*. Concretely:

1. **Forgery-channel completeness gate (88, 89):** at freeze, for every anti-oracle clause in the predicate ("sandbox hides the lane", "sees each gate only as an opaque launcher", "no file name visible"), commit at least one forgery control *per channel* (filesystem visibility, argv/usage text, digest identity, label table, timing excluded by declaration) and require it to read `unmet` in *every* layout the counting command will be run (canonical + clone, short + long scratch). The lane already runs both layouts post-freeze (r88 controls-clone-layout.txt; r89 both-layout controls) — the gate must make the clone-layout result blocking at freeze, not informational after scoring. QUALITY 126 (error rows = could-not-evaluate) is the code half; the process half is: no layout, no freeze.
2. **Determinism gate (88):** any randomised family must draw its critical case deterministically (CR at least once per run, r88 routed 2) or be excluded from the kill rule. A 2.6% per-run escape probability on a 3-run target is a flake factory; the gate should compute the escape probability from the draw parameters and reject random draws on kill families.
3. **Source-fidelity gate (90):** every rule in the battery docstring that is derived from pinned source must carry a clause→source-line map verified by a reviewer *before* freeze (the QUALITY 125 map exists; it must be frozen *with* the battery, not after). R10/R6 whole-file visibility would have been falsified at freeze by config.c 642–650. The lane's ReviewSource seat found it post-freeze; the gate moves that seat's check to freeze time for any rule sourced from a file the lane has not yet re-pinned at the installed tag.

Why this is catchable in-lane: in all three rounds the lane's own wave found the defect and the L1 correctly reported NOT VERIFIED. The failure was not blindness; it was that the declaration and the counting command were frozen before the wave, so the round had to file a known-false predicate as "target met, not verified" and take the honest-stop rejection. A pre-file gate that blocks freezing a predicate whose anti-oracle / fidelity clauses lack a committed, both-layouts, able-to-fail control converts the honest-stop into a pre-freeze fix.

[INFERENCE] The 3-rejection pause (Amendments 46/47/58) will not fix this: the mechanism is not exhaustion but predicate breadth — each round the lane widened the predicate (isolation → opaque launcher → full rule-set fidelity) faster than the frozen controls. The successor round must *narrow* the predicate to what the frozen instrument can enforce, or add the missing controls before freezing.

