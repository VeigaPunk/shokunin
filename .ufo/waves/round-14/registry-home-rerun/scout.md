# Registry-home reconnaissance (protocol round 14, registry-home-rerun)

Role: `R14HomeScout` — read-only. Sole artifact: this file. No sibling execution, no edits,
no builds/tests/lint/formatters, no commits. `closure-check.py` was **not** run (inherited
known failure: `TypeError` comparing `None` and `int` from a historical `round: null`).

Baseline carried from `.ufo/waves/round-14/registry-home-rerun/before.json`:
`measured_commit 99efc52b3a6f3648f7d8e097d78460901ad3c91c`,
`protocol_registered_closure_gates=0`, `root_SKILL_exists=False`,
`SCORECARD.md#aggregator-section = 7abc0478…5cfccf`,
`.ufo/reports/round-14/protocol.md = d2567df3…f691b4` (340 B).

---

## 1. Actual registries vs prose mentions

### 1a. Landed child registries — exactly ONE, not two

Definitive sweep over **every** `SKILL.md` in the tree (hidden + gitignored visible, so child
repos are included), pattern `^\|[^|]*\|\s*(?:gate|probe)\s*\|`:

```
grep path='**/SKILL.md' gitignore=false pattern='^\|[^|]*\|\s*(?:gate|probe)\s*\|'
→ one file only: chousa-shokunin/SKILL.md
```

`chousa-shokunin/SKILL.md`:

| Line | Bytes |
|---|---|
| 61 | `## Gates` (prose paragraph, 63–66) |
| 68 | `## Gates` (table section) |
| 70 | `\| name \| kind \| entry \| verdict map \| self-test \| pinned values \| write scope \| owner \|` |
| 71 | separator row |
| 72 | `\| \`research-gate\` \| gate \| \`bash tools/research-gate.sh verify <record>\` \| 0 clean (RESEARCH_GATE: CLEAN) · 1 failed (DRIFT) · 2 could-not-evaluate (setup/usage) \| \`bash tools/research-gate.sh --selftest\` → RESEARCH_GATE_SELFTEST: PASS (17 cases) \| hermetic cases in the script (\`/tmp/chousa-research-gate-selftest.*\`) \| live: zero writes; selftest: its own temp dir; no network \| chousa \|` |

**Field-name divergence (observed, not judged):** the landed header spells field 2 `kind`
(value `gate`) and renames two more columns — `entry` (schema: *entry command*) and
`pinned values` (schema: *pinned-value path*). Count is 8 either way. `PROTOCOL.md:383` names
the column literally ``gate|probe``; the child's spelling is the fleet's only landed convention.

### 1b. Everything else is prose or an unlanded draft

| Site | Kind | Evidence |
|---|---|---|
| `mori-shokunin/SKILL.md:47-51` | **prose claim, no row** — `## Gates` … `exit 2 for setup/usage. Registry row lands with the gate.` | grep of mori tree |
| `.ufo/waves/shokunin12h-20261014-p4-mori-r1/members/GateRegistryRow.md:58,66-68` | unlanded main-repo member **draft** (section §"Markdown table form": `name \| kind \| entry command \| verdict map \| self-test \| pinned-value path \| write scope \| owner`) | read of draft |
| `.ufo/waves/shokunin12h-20261014-p5-chousa-r1/members/GateRegistryRow.md:62,70-72` | same class, chousa's own draft (identical header, incl. `kind`) | grep, pattern `^\| *name *\|.*(entry command\|verdict map).*\|` |
| `kagi-shokunin/SKILL.md`, `kotoba-shokunin/SKILL.md`, `kengaku-shokunin/SKILL.md`, `kumitate-shokunin/SKILL.md`, `kake-shokunin/SKILL.md`, `kasegi-shokunin/SKILL.md` | **zero registry rows** | `.ufo/waves/round-13/connector-overlap.md:50` (`ALL-8` census, `total rows=0`) and `.ufo/waves/round-14/scratch/simplifier.md:62-66` (sweep → "no lines"); re-confirmed by §1a sweep |
| `mado-shokunin/SKILL.md:645-648`, `tsukuroi-shokunin/SKILL.md:1273-1275` | **prose verdict-mapping mentions** (drift classes → verdict; gate-verdict fold), not registries | grep `verdict map\|verdict mapping` |
| `kumitate-shokunin/SCORECARD.md` (`S1…S8`, `R1…R11` rows), counted by `scripts/proxy-check.mjs` `RE_REGISTRY_ROW=/^\| (S\|R)\d+ \|/` | **different meaning of "registry"** — a coverage registry over corpus sections, not a gate registry | `kumitate-shokunin/LOG.md:464-468`; `SCORECARD.md:346-348` |
| `chousa-shokunin/corpus/knowledge/*`, `revenger/game-dev-*` tables (`arm \| gate \| n`) | unrelated data tables containing the token `gate` | broad `\|\s*(?:gate\|probe)\s*\|` sweep |

### 1c. Main-repo registry — none exists

```
ls /home/vgpnk/Projects/shokunin/{SKILL.md,PROVINCE.md,SHONEN.md}  → No such file or directory (exit 2)
ls *.md *.json → AXES.md CORPUS.md LEARNING.md LOG.md MANIFEST.json MISSION.md
                 PROTOCOL-APPENDIX.md PROTOCOL.md README.md ROADMAP.md SCORECARD.md
```

Root `SCORECARD.md` carries **no** gate-registry table (baseline counts 0 rows beginning
`| closure-check | gate |` before `## Aggregator lane`). The only main-repo artifact that calls
itself a registry of record is `.ufo/reports/AGGREGATE.md`, the **routed-defect ledger**
(§11.2 heading at line 637; `D-` row keys), which `PROTOCOL.md:384-385` explicitly excludes as
an inventory: *"The aggregator ledger stays the routed-defect queue, not a second inventory."*

## 2. Convention to reuse (schema + home + ownership)

**Schema authority** — `PROTOCOL.md:382-387` (`## Gate standard` starts at `PROTOCOL.md:359`):

> `- **Registry.** The schema is this section's; the rows live in each lane's `SKILL.md`: name,
>   `gate|probe`, entry command, verdict map (code → class), self-test command and spelling,
>   pinned-value path, write scope, owner. The aggregator ledger stays the routed-defect queue, not a
>   second inventory; a fleet index is pointers to lane rows, never copied expected values. Frozen
>   baseline names resolve under any `.ufo/waves/*/frozen` root; a bare name matching more than one
>   root fails closed.`

**Delivery authority** — `PROTOCOL.md:399-402`:

> `- **Delivery.** This section reaches a lane through the re-read duty, not the driver's prompt
>   template (one of five child-lane items): … closure grades no gate conformant until its registry
>   row exists in the lane's own `SKILL.md`.`

Both clauses are **anchored on `SKILL.md`** (382 "rows live in each lane's `SKILL.md`";
401–402 "the lane's own `SKILL.md`"). For `protocol` and `aggregator` that anchor is unresolvable:
they are the two main-repo lanes (`shokunin.conf:19-22` — `protocol|.|…`, `aggregator|.|…`;
`MISSION.md` §Fleet shape: "the two main-repo lanes point at the fleet root itself"), and the root
has no `SKILL.md` (§1c). Any wording that resolves them **and** keeps children resolving must
therefore be conditional, and must be mirrored in **both** clauses, or the Delivery check keeps
demanding a nonexistent file.

**Shared-file ownership already ruled** — root `SCORECARD.md` is one path for both main-repo
lanes: `SCORECARD.md:132` (`## Aggregator lane — axes: …`) and `:134-139` state the aggregator
section is the aggregator lane's and that *"Both main-repo lanes write this single path and respawn
independently"*, filing the collision as ledger **D-77** (`.ufo/reports/AGGREGATE.md:735`).
The ruling is at `.ufo/reports/round-11/protocol.md:241-248`:

> `4. **Shared main-repo `SCORECARD.md`/`LOG.md`** (ledger D-77): ruled — per-lane sections in the
>    single canonical path … each lane committing **only its own section's hunks**; the round-11
>    hunk-surgical staging (`55e23de`) is the reference method. … If a collision ever destroys work,
>    the fallback (per-lane files) becomes a file-contract change proposal.`

So "protocol lane puts its own subsection in its own part of the root `SCORECARD.md`" is the
**already-ruled** shape for main-repo lanes — not a new lane policy and not a new file.

Protocol-lane section layout in root `SCORECARD.md` (line numbers, HEAD 99efc52):
`:1` title/ownership header, `:27` `## Metrics`, `:93` `## Planned`, `:111` `## Retired`,
`:118` `## Move log`, `:130` `---`, `:132` `## Aggregator lane — …`.

## 3. Narrow non-regression checks for the new rule

### 3a. Child relocation — avoidable, and detectable

Chousa's row lives in its own repo (`chousa-shokunin/SKILL.md:68-72`); the six older gate-owning
lanes owe their own rows under the same clause. A rule spelled unconditionally
("rows live in the root `SCORECARD.md`") or permissively ("a lane MAY register there") relocates
them, and then `PROTOCOL.md:401-402` ("the lane's own `SKILL.md`") contradicts the schema.

Verified non-regression test (byte-level, no execution of any gate):

```
git -C chousa-shokunin diff --stat -- SKILL.md     # expect empty
```

Falsifier for a *correct* rule: any child `SKILL.md` registry row that no longer satisfies
"its registry row exists in the lane's own `SKILL.md`". Safe wording form (evidence-matched, not
prescribed): the home rule stays "each lane's `SKILL.md`" with a single carve-out keyed on the
absence of a repository `SKILL.md`.

### 3b. Aggregator ledger — must not acquire a registry grant

Three independent sources forbid `.ufo/reports/AGGREGATE.md` as a home:
`PROTOCOL.md:384-385` (ledger = routed-defect queue, not an inventory);
`.ufo/reports/AGGREGATE.md:735` (D-77, aggregator-owned); and the durability record — the
ledger's own sibling class, a lane **report path**, has already been overwritten by closeout
markers 5 times, one of them *this lane's* `protocol r14` marker
(`SCORECARD.md:303` and `:348`: `5 marker-overwrite (kotoba r15 … 273 B vs 14,715 B at 4419fb9;
kengaku r12 274 B; protocol r13 275 B; protocol r14 340 B; kasegi r16 273 B)`).
A registry row placed on a marker-overwritable path can be destroyed by an unrelated lane round.
Non-regression checks: the new clause's home list must not contain `AGGREGATE.md`;
`.ufo/reports/AGGREGATE.md` byte-identity + `.ufo/reports/round-14/protocol.md` prefix bytes
(340 B, sha256 `d2567df3f11018ebd168918c46c7ea69119e45e41ac2f58140b1bf5634f691b4`) unchanged.

### 3c. Protected aggregator bytes — boundary reproducibly derived

`before.json`'s `SCORECARD.md#aggregator-section` digest is exactly
`sha256(SCORECARD.md.split("## Aggregator lane", 1)[1])`:

```
$ python3 -c 'import hashlib,pathlib;t=pathlib.Path("SCORECARD.md").read_text();
p=t.split("## Aggregator lane",1)[1];
print(len(p), hashlib.sha256(p.encode()).hexdigest())'
34622 7abc0478efcb16d0d2e4bbe57271d52c00da08a8eb33bc76edc272ae5b5cfccf
```

Consequences, all verified:
- The protected span starts **after** the literal string `## Aggregator lane` (byte offset
  **19658**), so it includes the rest of that heading line (` — axes: cross-lane quality, …`),
  the ownership paragraph, every aggregator section, and all trailing bytes.
- The `---\n\n` separator at `SCORECARD.md:130` and everything above it are **outside** that
  digest. The contract's "protocol registry subsection stays before `## Aggregator lane`" is
  therefore satisfiable by inserting into the protocol section (safest: a new `###` subsection
  ending before line 130, leaving the separator where it is); the digest alone would not catch a
  move of the separator, so the separator's position is a separate, explicitly-checked invariant.

### 3d. Pinned-value path convention (row field 6)

Two `frozen` roots exist today, which is why §Registry's last sentence exists:

```
.ufo/waves/round-12/frozen/{pre,post,post-actual}
.ufo/waves/round-15/frozen/{r15-pre-003400,r15-post-012710}   # 7 files each incl. expected.json
```

`closure-check.py:171-173` (`--frozen NAME searches every .ufo/waves/*/frozen root newest-first and
fails closed (exit 3) when a bare NAME matches more than one; disambiguate with --frozen
<wave>/<NAME>`) and `:1005-1027` (`_resolve_frozen`: duplicate bare name → ambiguity error;
`"<wave>/<NAME>"` resolved directly). The round-14 contract's qualified names
`round-15/r15-pre-003400` / `round-15/r15-post-012710` are exactly that disambiguating form;
round-12's `pre`/`post` names make the bare words ambiguous, so an unqualified citation is the
failure mode to avoid. Present binaries/digests: `.ufo/waves/round-15/closure-check.py`
sha256 `0ac440f7…9a778c`; `…/r15-pre-003400/expected.json` `19d6935b…2ddea9`;
`…/r15-post-012710/expected.json` `ba78759b…602315` (`before.json`).

### 3e. Status semantics are already correct without new policy

`PROTOCOL.md:393-398` (Closure consequence) makes a red gate a *routed, status-neutral*
conformance defect and says the integrator verifies committed evidence rather than executing a
sibling's gate. That is the clause backing "registration is not blanket conformance" — no new lane
policy is needed for that property.

## 4. Unresolved gaps / flags

1. **The dispatch premise "eight-field tables in two or more child skills" is not true of the
   landed fleet.** Exactly one child `SKILL.md` holds such a table (chousa). The other two rows are
   unlanded main-repo member drafts (mori p4-r1, chousa p5-r1). Reported as observed; the
   convention comparison therefore rests on one landed row + two drafts + the protocol schema.
2. **Field-2 spelling is divergent** (`kind` landed vs ``gate|probe`` in `PROTOCOL.md:383`), and
   1a shows two more column renames. If the new rule restates the eight names, it should not
   silently re-pin the child's wording nor claim the child row matches the schema verbatim.
3. **`chousa-shokunin/SKILL.md` has two identical `## Gates` headings** (lines 61 and 68) — any
   pointer convention of the form "the lane's Gates section" is ambiguous there.
4. **"Registry row" is overloaded in-fleet** (`kumitate` coverage rows vs gate rows). The protocol
   text qualified it as §Gate standard's registry; a new clause relying on bare "registry" invites
   the kumitate reading.
5. **Not exercised (by contract):** `closure-check.py` self-test/frozen replay and the live gate
   crash; the aggregator-section digest was reproduced statically, not by running the parent's
   verifier.

## 5. Commands used (all read-only)

```
grep '**/SKILL.md' gitignore=false '^\|[^|]*\|\s*(?:gate|probe)\s*\|'        # §1a, one hit
grep '*-shokunin/SKILL.md' gitignore=false 'verdict map|entry command|pinned-value path'
grep '.' gitignore=false '^\| *name *\|.*(entry command|verdict map).*\|'    # drafts
ls /home/vgpnk/Projects/shokunin/{SKILL.md,PROVINCE.md,SHONEN.md}            # absent (exit 2)
ls .ufo/waves/*/frozen/*                                                     # two roots
wc -c .ufo/reports/round-14/protocol.md; sha256sum …                         # 340 B, d2567df3…
python3 -c 'split("## Aggregator lane",1)[1] → sha256'                       # §3c, matches before.json
```