#!/usr/bin/env bash
# jj-lane-selftest.sh — sandboxed proof of scripts/hyaku/jj-lane.sh.
#
#   jj-lane-selftest.sh [lane-repo]
#
# Builds a bare remote + clones of a REAL lane repo ($1, default
# kake-shokunin) under mktemp -d /fast/scratch/jj-hyaku.XXXXXX — the only
# contact with the live repo is `git clone` reading it; nothing is pushed to
# a real remote and no jj command runs inside a live lane. Prints one
# PASS/FAIL line per case and `selftest <passed>/<total>`; exit 0 iff all pass.
set -u

SRC=${1:-/home/vgpnk/Projects/shokunin/kake-shokunin}
HELPER=$(cd "$(dirname "$0")" && pwd)/jj-lane.sh
JJ=${JJ_BIN:-$(command -v jj 2>/dev/null || echo "$HOME/.local/bin/jj")}

mkdir -p /fast/scratch
SB=$(mktemp -d /fast/scratch/jj-hyaku.XXXXXX) || { echo "sandbox failed" >&2; exit 1; }
cleanup() { if [ "${KEEP_SB:-0}" = 1 ]; then echo "sandbox kept: $SB" >&2; else rm -rf "$SB"; fi; }
trap cleanup EXIT

export HYAKU_STATE="$SB/state"
mkdir -p "$HYAKU_STATE"

[ -d "$SRC/.git" ] || { echo "FAIL missing source lane repo $SRC" >&2; exit 1; }
[ -x "$HELPER" ] || { echo "FAIL missing helper $HELPER" >&2; exit 1; }

pass=0 total=0
check() { # <label> <0|1>
  total=$((total + 1))
  if [ "$2" -eq 0 ]; then echo "PASS $1"; pass=$((pass + 1)); else echo "FAIL $1"; fi
}
rc() { if [ "$1" -eq 0 ]; then echo 0; else echo 1; fi }

REMOTE="$SB/remote.git"
git clone --bare -q "$SRC" "$REMOTE"
LANE_ID=testlane
IDENT_NAME="${LANE_ID}-shokunin"
IDENT_MAIL="${LANE_ID}@shokunin.local"

mkclone() { # <name> — fresh clone wired to the sandbox remote
  git clone -q "$REMOTE" "$SB/$1"
  git -C "$SB/$1" remote set-url origin "$REMOTE" >/dev/null 2>&1 || true
}

branch_of() { git -C "$1" symbolic-ref -q refs/remotes/origin/HEAD | sed 's|.*/||'; }

jcfg() { cat "$HOME/.config/jj/repos/$(cat "$1/.jj/repo/config-id")/config.toml" 2>/dev/null; }


# operator-style commit on the remote through a separate clone (pull-rebase
# first so it tracks whatever the lanes have already pushed).
op_commit() { # <file> <content>
  local d="$SB/op" f=$1 c=$2
  if [ ! -d "$d" ]; then mkclone op; git -C "$d" config user.name operator; git -C "$d" config user.email op@sandbox.local; fi
  git -C "$d" pull -q --rebase origin "$(branch_of "$d")"
  echo "$c" > "$d/$f"
  git -C "$d" add "$f" && git -C "$d" commit -qm "operator: $f" && git -C "$d" push -q origin HEAD
}

#############################################################################
# a. init on a plain git clone: .jj created, config present; re-init no-op.
mkclone a
"$HELPER" init "$SB/a" "$LANE_ID" >/dev/null 2>&1
ok=0
[ -d "$SB/a/.jj" ] || ok=1
jcfg "$SB/a" | grep -q "name = \"$IDENT_NAME\"" || ok=1
jcfg "$SB/a" | grep -q "email = \"$IDENT_MAIL\"" || ok=1
jcfg "$SB/a" | grep -q 'auto-track = "none()"' || ok=1
jcfg "$SB/a" | grep -q '"trunk()" = "master@origin"' || ok=1
"$HELPER" init "$SB/a" "$LANE_ID" >/dev/null 2>&1 || ok=1
[ -d "$SB/a/.jj" ] || ok=1
check "a init+reinit" "$ok"

# b. pre-existing ::bookmarks() immutable alias survives init.
mkclone b
(cd "$SB/b" && "$JJ" --config 'snapshot.auto-track="none()"' git init --colocate . >/dev/null 2>&1)
cid=$(cat "$SB/b/.jj/repo/config-id")
cat > "$HOME/.config/jj/repos/$cid/config.toml" <<EOF
[revset-aliases]
"trunk()" = "master@origin"
"immutable_heads()" = "builtin_immutable_heads() | ::bookmarks()"
EOF
"$HELPER" init "$SB/b" "$LANE_ID" >/dev/null 2>&1
ok=0
jcfg "$SB/b" | grep -q 'immutable_heads()" = "builtin_immutable_heads() | ::bookmarks()"' || ok=1
jcfg "$SB/b" | grep -q "name = \"$IDENT_NAME\"" || ok=1
check "b keeps-immutable-alias" "$ok"

# c-f. pathspec commit on clone a.
A="$SB/a"; BR=$(branch_of "$A")
printf 'a-change\n' >> "$A/README.md"          # A: tracked, modified -> commit
printf 'b-change\n' >> "$A/LOG.md"             # B: tracked, modified -> stays
echo newfile > "$A/NEWFILE-$RANDOM.txt"        # N: untracked -> commit
echo scratch > "$A/SCRATCH-$$.tmp"             # S: untracked -> stays
N="NEWFILE-$RANDOM.txt"; echo newfile > "$A/$N"; S="SCRATCH-$$.tmp"; echo scratch > "$A/$S"
out=$("$HELPER" commit "$A" --as "$LANE_ID" -m "selftest c" -- README.md "$N" 2>/dev/null)
CHASH=$(printf '%s\n' "$out" | sed -n 's/^committed //p' | head -1)
PHASH=$(printf '%s\n' "$out" | sed -n 's/^pushed //p' | head -1)
ok=0
[ -n "$CHASH" ] || ok=1
[ "$(git -C "$A" show --format= --name-only "$CHASH" 2>/dev/null | sort | xargs)" = "README.md $N" ] || \
  { git -C "$A" show --format= --name-only "$CHASH" | grep -qx 'README.md' \
    && git -C "$A" show --format= --name-only "$CHASH" | grep -qx "$N" \
    && [ "$(git -C "$A" show --format= --name-only "$CHASH" | wc -l)" -eq 2 ] || ok=1; }
[ "$(git -C "$A" cat-file -p "$CHASH:README.md" | tail -1)" = "a-change" ] || ok=1
[ "$(git -C "$A" show "$CHASH:LOG.md" | tail -1)" != "b-change" ] || ok=1  # B not in commit
[ "$(tail -1 "$A/LOG.md")" = "b-change" ] || ok=1                        # B intact on disk
[ "$(cat "$A/$S")" = "scratch" ] || ok=1                                 # S intact on disk
git -C "$A" status --porcelain | grep -q "^?? $S\$" || ok=1              # S still untracked
git -C "$A" status --porcelain | grep -q "^ M LOG.md\$" || ok=1          # B still modified
check "c pathspec-commit" "$ok"

line=$(git -C "$A" log -1 --format='%an|%ae|%cn|%ce' "$CHASH" 2>/dev/null)
if [ "$line" = "$IDENT_NAME|$IDENT_MAIL|$IDENT_NAME|$IDENT_MAIL" ]; then ok=0; else ok=1; fi
check "d lane-identity" "$ok"



ok=0
[ "$(git -C "$A" rev-parse "$BR")" = "$CHASH" ] || ok=1
[ "$(git -C "$A" log -1 --format=%H -- README.md)" = "$CHASH" ] || ok=1
git -C "$A" merge-base --is-ancestor "$CHASH" HEAD || ok=1
head_kind=detached; git -C "$A" symbolic-ref -q HEAD >/dev/null 2>&1 && head_kind=attached
echo "  (git HEAD after jj commit: $head_kind)"
check "e git-interop" "$ok"

ok=0
[ -n "$PHASH" ] || ok=1
[ "$(git -C "$REMOTE" rev-parse "refs/heads/$BR")" = "$PHASH" ] || ok=1
[ "$PHASH" = "$CHASH" ] || ok=1
"$HELPER" push "$A" >/dev/null 2>&1 || { [ "$(git -C "$REMOTE" rev-parse "refs/heads/$BR")" = "$PHASH" ]; }
[ "$(cd "$A" && git rev-list --count "origin/$BR..$BR")" = "0" ] || ok=1
"$HELPER" state "$A" | grep -q 'ahead=0' || ok=1
check "f push-landed" "$ok"

# d2. --as protocol yields protocol-shokunin on author AND committer.
mkclone d2
"$HELPER" init "$SB/d2" "$LANE_ID" >/dev/null 2>&1
echo proto > "$SB/d2/PROTO.md"
out=$("$HELPER" commit "$SB/d2" --as protocol -m "closure" -- PROTO.md 2>/dev/null)
ph=$(printf '%s\n' "$out" | sed -n 's/^committed //p' | head -1)
line=$(git -C "$SB/d2" log -1 --format='%an|%ae|%cn|%ce' "$ph" 2>/dev/null)
if [ "$line" = "protocol-shokunin|protocol@shokunin.local|protocol-shokunin|protocol@shokunin.local" ]; then ok=0; else ok=1; fi
check "d protocol-identity" "$ok"

# g. remote moved by operator -> helper commit+push recovers via fetch+rebase.
op_commit OP-G.md "operator-g"
echo lanework > "$A/LANE-G.md"
out=$("$HELPER" commit "$A" --as "$LANE_ID" -m "selftest g" -- LANE-G.md 2>/dev/null)
PH=$(printf '%s\n' "$out" | sed -n 's/^pushed //p' | head -1)
ok=0
[ -n "$PH" ] || ok=1
remote_log=$(git -C "$REMOTE" log --format='%H %s' "$BR")
printf '%s\n' "$remote_log" | grep -q "$PH" || ok=1
printf '%s\n' "$remote_log" | grep -q 'operator: OP-G.md' || ok=1
# operator commit untouched: its subject+files unchanged and it is an ancestor
git -C "$REMOTE" merge-base --is-ancestor "$(git -C "$REMOTE" rev-parse "$BR~1" 2>/dev/null)" "$BR" 2>/dev/null || true
op_hash=$(git -C "$REMOTE" log --format=%H -1 --grep='operator: OP-G.md' "$BR")
[ -n "$op_hash" ] && git -C "$REMOTE" merge-base --is-ancestor "$op_hash" "$PH" || ok=1
check "g fetch-rebase-recovery" "$ok"

# h. same recovery with the ::bookmarks() immutable alias configured.
B="$SB/b"
# h commits only a new file so the recovery rebase cannot hit a text conflict.
echo laneh > "$B/LANE-H.md"
op_commit OP-H.md "operator-h"
out=$("$HELPER" commit "$B" --as "$LANE_ID" -m "selftest h" -- LANE-H.md 2>/dev/null)
PH=$(printf '%s\n' "$out" | sed -n 's/^pushed //p' | head -1)
ok=0
[ -n "$PH" ] || ok=1
git -C "$REMOTE" log --format=%H "$BR" | grep -q "$PH" || ok=1
git -C "$REMOTE" log --format=%s "$BR" | grep -q 'operator: OP-H.md' || ok=1
jcfg "$B" | grep -q 'immutable_heads()" = "builtin_immutable_heads() | ::bookmarks()"' || ok=1
check "h immutable-alias-recovery" "$ok"

# i. plain git commit in colocated clone imported by next helper commit.
mkclone i
"$HELPER" init "$SB/i" "$LANE_ID" >/dev/null 2>&1
echo direct > "$SB/i/DIRECT.md"
git -C "$SB/i" -c user.name=op -c user.email=op@x commit -qm "direct git commit" -- DIRECT.md 2>/dev/null \
  || { git -C "$SB/i" add DIRECT.md && git -C "$SB/i" -c user.name=op -c user.email=op@x commit -qm "direct git commit"; }
echo lanei > "$SB/i/LANE-I.md"
out=$("$HELPER" commit "$SB/i" --as "$LANE_ID" -m "selftest i" -- LANE-I.md 2>/dev/null)
PH=$(printf '%s\n' "$out" | sed -n 's/^pushed //p' | head -1)
ok=0
[ -n "$PH" ] || ok=1
git -C "$REMOTE" log --format=%s "$BR" | grep -q 'direct git commit' || ok=1
git -C "$REMOTE" log --format=%s "$BR" | grep -q 'selftest i' || ok=1
[ -z "$(cd "$SB/i" && "$JJ" log --ignore-working-copy --no-graph -T x -r 'divergent()' 2>/dev/null)" ] || ok=1
(cd "$SB/i" && "$JJ" bookmark list --ignore-working-copy 2>/dev/null | grep -q 'conflict') && ok=1
check "i git-commit-import" "$ok"

# j. big untracked files.
mkclone j
head -c 5242880 /dev/urandom > "$SB/j/BIG.bin"
head -c 2097152 /dev/urandom > "$SB/j/MED.bin"
"$HELPER" init "$SB/j" "$LANE_ID" >/dev/null 2>&1
echo jx > "$SB/j/j.md"
out=$("$HELPER" commit "$SB/j" --as "$LANE_ID" -m "selftest j" -- j.md MED.bin 2>/dev/null)
PH=$(printf '%s\n' "$out" | sed -n 's/^pushed //p' | head -1)
ok=0
[ -n "$PH" ] || ok=1
"$HELPER" state "$SB/j" >/dev/null 2>&1 || ok=1
git -C "$SB/j" status --porcelain | grep -q '^?? BIG.bin' || ok=1   # BIG stays untracked
git -C "$REMOTE" show "$PH:MED.bin" >/dev/null 2>&1 || ok=1       # 2MiB committed
[ "$(git -C "$REMOTE" cat-file -s "$PH:MED.bin")" = "2097152" ] || ok=1
check "j big-files" "$ok"

# k. two concurrent helper commits on different paths.
mkclone k1; mkclone k2
"$HELPER" init "$SB/k1" "$LANE_ID" >/dev/null 2>&1
"$HELPER" init "$SB/k2" "$LANE_ID" >/dev/null 2>&1
echo k1 > "$SB/k1/K1.md"; echo k2 > "$SB/k2/K2.md"
"$HELPER" commit "$SB/k1" --as "$LANE_ID" -m "k1" -- K1.md >/dev/null 2>&1 &
p1=$!
"$HELPER" commit "$SB/k2" --as "$LANE_ID" -m "k2" -- K2.md >/dev/null 2>&1 &
p2=$!
r1=0; r2=0; wait $p1 || r1=$?; wait $p2 || r2=$?
ok=0
[ $r1 -eq 0 ] || ok=1
[ $r2 -eq 0 ] || ok=1
git -C "$REMOTE" show "$BR:K1.md" >/dev/null 2>&1 || ok=1
git -C "$REMOTE" show "$BR:K2.md" >/dev/null 2>&1 || ok=1
(cd "$SB/k1" && "$JJ" git fetch >/dev/null 2>&1)
[ -z "$(cd "$SB/k1" && "$JJ" log --ignore-working-copy --no-graph -T x -r 'divergent()' 2>/dev/null)" ] || ok=1
(cd "$SB/k1" && "$JJ" bookmark list --ignore-working-copy 2>/dev/null | grep -q 'conflict') && ok=1
check "k concurrent-commits" "$ok"

# l. state changes nothing.
mkclone l
"$HELPER" init "$SB/l" "$LANE_ID" >/dev/null 2>&1
echo dirty >> "$SB/l/README.md"
echo untracked > "$SB/l/u.tmp"
op_head() { (cd "$SB/l" && "$JJ" op log --ignore-working-copy -n1 --no-graph -T 'self.id()' 2>/dev/null); }
gstat() { git -C "$SB/l" status --porcelain; }
o1=$(op_head); s1=$(gstat)
"$HELPER" state "$SB/l" >/dev/null 2>&1
o2=$(op_head); s2=$(gstat)
ok=0
[ "$o1" = "$o2" ] || ok=1
[ "$s1" = "$s2" ] || ok=1
[ -n "$o1" ] || ok=1
check "l state-readonly" "$ok"

# m. git index interplay: staged entry across helper state+commit of a
# different path — reported either way, asserts only that the helper worked
# and the file content survived on disk.
mkclone m
"$HELPER" init "$SB/m" "$LANE_ID" >/dev/null 2>&1
echo staged-content > "$SB/m/STAGED.md"
git -C "$SB/m" add STAGED.md
staged_before=$(git -C "$SB/m" ls-files --error-unmatch STAGED.md >/dev/null 2>&1 && echo yes || echo no)
"$HELPER" state "$SB/m" >/dev/null 2>&1
staged_after_state=$(git -C "$SB/m" ls-files --error-unmatch STAGED.md >/dev/null 2>&1 && echo yes || echo no)
echo mfile > "$SB/m/M.md"
out=$("$HELPER" commit "$SB/m" --as "$LANE_ID" -m "selftest m" -- M.md 2>/dev/null)
PH=$(printf '%s\n' "$out" | sed -n 's/^pushed //p' | head -1)
staged_after_commit=$(git -C "$SB/m" ls-files --error-unmatch STAGED.md >/dev/null 2>&1 && echo yes || echo no)
echo "  (staged entry: before=$staged_before after-state=$staged_after_state after-commit=$staged_after_commit)"
ok=0
[ -n "$PH" ] || ok=1
[ -f "$SB/m/STAGED.md" ] && [ "$(cat "$SB/m/STAGED.md")" = "staged-content" ] || ok=1
check "m staged-index-interplay" "$ok"

# n. init on a dirty tree (seat scratch, operator sweep dir present) must not
# track anything: every untracked path stays "??" in git and absent from jj.
mkclone n
mkdir -p "$SB/n/census/opsweep" && echo o > "$SB/n/census/opsweep/a.txt"
echo u > "$SB/n/SCRATCH-N.tmp"
"$HELPER" init "$SB/n" "$LANE_ID" >/dev/null 2>&1
"$HELPER" init "$SB/n" "$LANE_ID" >/dev/null 2>&1
ok=0
[ "$(git -C "$SB/n" status --porcelain | grep -c '^??')" -eq 2 ] || ok=1
git -C "$SB/n" status --porcelain | grep -qv '^??' && ok=1
(cd "$SB/n" && "$JJ" file list --ignore-working-copy | grep -qE '^(SCRATCH-N.tmp|census/opsweep/a.txt)$') && ok=1
check "n dirty-init-tracks-nothing" "$ok"

# o. committing a named directory behaves like `git add <dir>`: ignored
# content inside it (caches, seat scratch) stays out of the commit.
mkclone o
"$HELPER" init "$SB/o" "$LANE_ID" >/dev/null 2>&1
mkdir -p "$SB/o/wave/__pycache__" && echo keep > "$SB/o/wave/keep.md" && echo junk > "$SB/o/wave/__pycache__/x.pyc"
echo '__pycache__/' >> "$SB/o/.git/info/exclude"
out=$("$HELPER" commit "$SB/o" --as "$LANE_ID" -m "selftest o" -- wave 2>/dev/null)
PH=$(printf '%s\n' "$out" | sed -n 's/^pushed //p' | head -1)
ok=0
[ -n "$PH" ] || ok=1
git -C "$REMOTE" ls-tree -r --name-only "$PH" -- wave | grep -qx 'wave/keep.md' || ok=1
git -C "$REMOTE" ls-tree -r --name-only "$PH" -- wave | grep -q '__pycache__' && ok=1
check "o dir-commit-skips-ignored" "$ok"

echo "selftest $pass/$total"
[ "$pass" -eq "$total" ]
