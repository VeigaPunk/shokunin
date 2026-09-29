# ClassCritic — adversarial measurement review

## 1. Runnable rows that can pass while the duty is violated

### Finding 1 — H1 is source-text/name satisfiable, not serialization-behaviour satisfiable

**Command executed** (fixture uses a temporary `HOME`; no repository or host file was changed):

```bash
d=$(mktemp -d)
mkdir -p "$d/.local/bin" "$d/.local/state/the-janitor"
printf '# flock 9\n# flock 9\nLOCK_FILE=not-a-lock\n' > "$d/.local/bin/the-janitor"
h1=$(awk -F '\t' '$1=="H1"{print $4}' corpus/checklist.tsv)
HOME="$d" bash -c "$h1"
```

**Observed output:**

```text
CLIENT_LOCK: flock=2 declared=1 mode=absent
```

The command exited 0. The fixture contains no executable lock acquisition at all: both matching strings are comments and the declared path is not used. H1's runnable check therefore certifies two spellings and an optional file mode, not that one request actually serializes another. The `mode=absent` allowance also makes absence of the lock artifact a passing state.

### Finding 2 — H8 has a narrow-file blind spot

**Command executed** (same style of temporary `HOME`; a password setting is placed in an unexamined environment file, while the two files named by H8 are empty):

```bash
printf 'OPENCODE_SERVER_PASSWORD=<fixture-value>\n' > "$d/.config/the-janitor/env"
: > "$d/.config/the-janitor/client.py"
h8=$(awk -F '\t' '$1=="H8"{print $4}' corpus/checklist.tsv)
HOME="$d" bash -c "$h8"
```

**Observed output:**

```text
CONTROL_PLANE: password_refs=0 listeners=0 non_loopback=0 established=0
```

The command exited 0. H8's duty is a control-plane safety rule, but the check only counts the password token in two specific files and observes sockets. A third configuration source can carry the setting while the row still returns clean. This is a measurement blind spot, not a claim that the live host currently has that setting.

### Finding 3 — a fully gameable 16-row declaration passes the gate

**Command executed:** a temporary TSV transformed every row to `runnable`, with command `printf "FAKE-<id>: OK\\n"`, matching expected exit/last-line, and the existing one-to-one leads. The real SKILL.md was supplied unchanged:

```bash
d=$(mktemp -d)
awk -F '\t' 'BEGIN{OFS="\t"} /^#/||NF==0{print;next} {$2="runnable";$4="printf \\"FAKE-"$1": OK\\n\\"";$5=0;$6="^FAKE-"$1": OK$";$7="-";$8="fixture filler: emits a verdict without checking the declared duty";print}' corpus/checklist.tsv > "$d/f.tsv"
bash corpus/checklist-run.sh --tsv "$d/f.tsv"
```

**Observed output:**

```text
CHECKLIST_RATIO: runnable=16/16 floor=8 by_hand=0
CHECKLIST_RUN: CLEAN (items=16 runnable=16 by_hand=0 failed=0)
```

Every checklist duty is violated by construction: no host, runtime, transcript, receipt, or cross-lane surface is inspected. The gate checks shape, exit, last line, lead bijection, and ratio; it does not check that a runnable command has any semantic relationship to its lead item. This is the strongest direct proof that `K` is a count of declared runnable rows, not a count of useful measurements.

## 2. A by-hand item that is cheaply mechanisable

### Finding 4 — H5's observable premise is already a cheap probe

H5 is classified `by-hand` for CDP/shared-profile lease adjudication. The judgement “report a conflict and do not absorb another lane's lease” is genuinely human/cross-lane. However, its objective premise (whether a listener/connection exists and whether the shared manifest is present) is cheap to observe and should not disappear behind the by-hand class.

**Command executed:**

```bash
printf 'listeners_9222='; ss -ltnH 2>/dev/null | awk '$4 ~ /:9222$/ {n++} END{print n+0}'
printf 'established_9222='; ss -tnH state established 2>/dev/null | awk '$4 ~ /:9222$/ || $5 ~ /:9222$/ {n++} END{print n+0}'
test -e "$HOME/.local/share/the-musketeer/chrome-profile/NativeMessagingHosts/com.1password.1password.json" && echo 'musketeer_manifest=present' || echo 'musketeer_manifest=absent'
```

**Observed output:**

```text
listeners_9222=0
established_9222=0
musketeer_manifest=present
```

A runnable H5-premise row can report these metadata-only facts; a separate by-hand decision can retain ownership/adjudication. The current one-row/one-item model forces the mechanisable premise and the human judgement to share one class, losing cheap evidence.

## 3. CHECKLIST_RATIO inflation

### Finding 5 — splitting and delegation make `K` dishonest

The live declaration reports `runnable=9/16`, `floor=8`, `by_hand=7`. The gate's only quantitative predicate is `K * 2 >= N`; it has no semantic weight for a row and no distinction between a novel probe, an existing gate invocation, and `printf`.

The 16-row filler fixture above proves the upper bound: a bad-faith author can report `K=16`, `N=16`, ratio 1.0, while checking zero duties. That is an inflation from the shipped `K=9` to `K=16` (+7 counted runnable rows; ratio +43.75 percentage points, 56.25% to 100%).

A less extreme split has the same problem. E1 already delegates to the surface and drift gates. A bad-faith author can split that one duty into separate census and drift rows (or add rows whose only command is an existing gate's invocation), then mark each as runnable. With the fixed 16-item bijection, extra rows are rejected, so the practical attack is not adding rows beyond 16; it is replacing by-hand rows or weakening existing rows with delegated/constant checks. The filler fixture demonstrates the maximum permitted by the current schema without violating the one-row-per-item shape.

The current schema also permits `expect_exit=0|1`; H7's expected baseline legitimately uses it, but a constant command plus `0|1` is non-discriminating. The last-line regex can likewise be broad. These are additional reasons not to treat `K` as measurement coverage without a quality gate.

## 4. By-hand lazy-map attack

The class plus unique-reason rule does **not** prevent a lazy map. A bad-faith author can assign all 16 rows `by-hand`, give each a distinct 24-character sentence, and satisfy uniqueness/shape — the only current blocker is the ratio floor, which requires at least 8 runnable rows. The all-filler fixture shows the converse: those 8 required runnable rows can be semantic no-ops, leaving the other 8 (or the current 7) by-hand.

The five closed classes do not solve this: 16 unique notes are easy, and pigeonhole pressure merely means several rows share a class. The class labels describe why an author says “by-hand”; they do not prove that no cheap probe exists.

## Recommended guards

1. **Pin the item map and separate premise from judgement.** Keep the 16-item bijection, but permit a checklist item to have multiple evidence rows (or allow a runnable premise row plus a by-hand decision row). H5 should retain a by-hand ownership decision while also recording a metadata-only socket/profile probe.
2. **Reject constant/self-verdict runnable checks.** In `load_rows`, reject commands whose normalized form only prints a fixed verdict (`printf`, `echo`, or `true`) and does not read/execute an allowed evidence surface. Require a command-specific evidence token in the note and require the command to name that surface.
3. **Add a delegation rule.** A row that invokes another `corpus/*.sh` gate must declare a distinct defect signal not already represented by that gate's own verdict. Better: count delegated rows separately (`delegated=D`) and do not let them satisfy the non-delegated runnable floor without review. This prevents re-asserting an existing gate's exit from inflating coverage.
4. **Add a negative-fixture requirement.** Every runnable row should have a selftest mutation in which its named surface is made defective and the row must fail. A constant-output row cannot supply such a mutation. This is stronger than regex lint and directly attacks the observed filler fixture.
5. **Make ratio honest with a fixed denominator and quality floor.** Keep `N=16` via the lead bijection, but report `runnable`, `delegated`, `by_hand`, and `quality_checked`; require `quality_checked >= floor`. Do not count a row merely because it is syntactically runnable. Pin the floor monotonically so it cannot be lowered as the checklist evolves.
6. **Fence the by-hand class with a hard quota plus proof obligation.** Require each by-hand note to include a concrete external obstacle and an explicit “what would mechanise it” clause, then enforce a quota (for example `by_hand <= 4` if the intended floor is 12/16). Independently reject by-hand classification when the item text names an existing command whose exit is its own defect signal, unless a review exception is recorded.
7. **Add per-class quotas as a backstop, not the sole proof.** A cap of three rows per by-hand reason class would prevent 16-by-hand (five classes × three = 15), but it still does not establish semantic necessity; combine it with the quota and negative-fixture rules above.
8. **Keep E4's exclusions closed and audited.** The ref-shaped scan currently uses named placeholder exclusions; every exclusion must be a fixture-specific, path-specific exception, not a freely extensible vault-name allowlist. Otherwise an author can make a prohibited artifact look like a placeholder and preserve a clean verdict.

