#!/usr/bin/env bash
# jj-lane-selftest.sh — sandboxed proof of scripts/hyaku/jj-lane.sh.
#
#   jj-lane-selftest.sh [lane-repo]
#
# Builds a bare remote + clones of a REAL lane repo ($1, default
# kake-shokunin) under /tmp/jj-hyaku.XXXXXX — the only contact with the
# source is `git clone` reading it; nothing is pushed to a real remote and no
# jj command runs inside a live lane. Prints one PASS/FAIL line per case and
# `selftest <passed>/<total>`; exit 0 iff all pass.
#
# Every case runs against the working helper and the HEAD helper extracted into
# the sandbox. Older behavior is diagnostic by default; only cases explicitly
# marked as regressions require the HEAD helper to fail.
set -u

SRC=${1:-/home/vgpnk/Projects/shokunin/kake-shokunin}
SELF_DIR=$(cd "$(dirname "$0")" && pwd -P)
HELPER=${HELPER:-$SELF_DIR/jj-lane.sh}
JJ=${JJ_BIN:-$(command -v jj 2>/dev/null || echo "$HOME/.local/bin/jj")}

# Ignore inherited repository selectors/configuration; test Git/JJ state is
# sandbox-only even when invoked from a live colocated lane or with GIT_DIR set.
for name in ${!GIT_@}; do unset "$name"; done
for name in ${!JJ_@}; do [ "$name" = JJ_BIN ] || unset "$name"; done
export GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL=/dev/null
export JJ_BIN="$JJ"

SB=$(mktemp -d /tmp/jj-hyaku.XXXXXX) || { echo "sandbox failed" >&2; exit 1; }
# Isolate jj's global configuration as well as every clone and bare remote.
export HOME="$SB/home"
export XDG_CONFIG_HOME="$HOME/.config"
mkdir -p "$XDG_CONFIG_HOME"
# jj keeps per-repo config in $HOME/.config/jj/repos/<config-id>/; init writes
# there, so drop exactly the entries belonging to our sandbox clones before
# removing the sandbox.
cleanup() {
  local c id
  for c in "$SB"/*/; do
    [ -f "$c.jj/repo/config-id" ] || continue
    id=$(cat "$c.jj/repo/config-id" 2>/dev/null) || continue
    [ -z "$id" ] || rm -rf "$HOME/.config/jj/repos/$id"
  done
  if [ "${KEEP_SB:-0}" = 1 ]; then echo "sandbox kept: $SB" >&2; else rm -rf "$SB"; fi
}
trap cleanup EXIT

export HYAKU_STATE="$SB/state"
mkdir -p "$HYAKU_STATE"

[ -d "$SRC/.git" ] || { echo "FAIL missing source lane repo $SRC" >&2; exit 1; }
[ -x "$HELPER" ] || { echo "FAIL missing helper $HELPER" >&2; exit 1; }

OLD="$SB/jj-lane-old.sh"
if ! { git -C "$SELF_DIR/../.." show HEAD:scripts/hyaku/jj-lane.sh > "$OLD" 2>/dev/null && chmod +x "$OLD"; }; then
  echo "FAIL cannot extract old helper" >&2; exit 1
fi

pass=0 total=0
check() { # <label> <0|1>
  total=$((total + 1))
  if [ "$2" -eq 0 ]; then echo "PASS $1"; pass=$((pass + 1)); else echo "FAIL $1"; fi
}

REMOTE="$SB/remote.git"
new_remote() { # fresh bare remote; every prior clone's origin is re-pointed
  rm -rf "$REMOTE"
  git clone --bare -q "$SRC" "$REMOTE"
  for c in "$SB"/*/; do
    [ -d "${c}.git" ] && git -C "$c" remote set-url origin "$REMOTE" >/dev/null 2>&1
  done
  return 0
}
new_remote
LANE_ID=testlane
IDENT_NAME="${LANE_ID}-shokunin"
IDENT_MAIL="${LANE_ID}@shokunin.local"

mkclone() { # <name> — fresh clone wired to the sandbox remote
  git clone -q "$REMOTE" "$SB/$1"
  git -C "$SB/$1" remote set-url origin "$REMOTE" >/dev/null 2>&1 || true
}

BR=$(git -C "$REMOTE" symbolic-ref -q HEAD 2>/dev/null | sed 's|refs/heads/||')
[ -n "$BR" ] || BR=$(git -C "$REMOTE" for-each-ref --format='%(refname:short)' refs/heads/ | head -1)

jcfg() { cat "$HOME/.config/jj/repos/$(cat "$1/.jj/repo/config-id")/config.toml" 2>/dev/null; }

# operator-style commit on the remote through a separate clone.
op_commit() { # <file> <content>
  local d="$SB/op" f=$1 c=$2
  if [ ! -d "$d" ]; then mkclone op; git -C "$d" config user.name operator; git -C "$d" config user.email op@sandbox.local; fi
  git -C "$d" pull -q --rebase origin "$BR" 2>/dev/null || git -C "$d" pull -q --rebase origin "$BR"
  echo "$c" > "$d/$f"
  git -C "$d" add "$f" && git -C "$d" commit -qm "operator: $f" && git -C "$d" push -q origin "HEAD:$BR"
}

remote_tip() { git -C "$REMOTE" rev-parse "refs/heads/$BR" 2>/dev/null; }

# Run one scenario function against BOTH helpers on fresh clones. $D = clone
# dir, $H = helper for the body's run. Set the third arg only for a regression
# that must fail against the HEAD baseline.
D=; H=
try_both() { # <label> <function> [expect-old-failure]
  local label=$1 fn=$2 expect_old_fail=${3:-0} ok_new ok_old
  new_remote
  mkclone "${label}-new"; D="$SB/${label}-new"; H="$HELPER"
  ( $fn ) >/dev/null 2>"$SB/${label}.new.err"; ok_new=$?
  new_remote
  mkclone "${label}-old"; D="$SB/${label}-old"; H="$OLD"
  ( $fn ) >/dev/null 2>"$SB/${label}.old.err"; ok_old=$?
  local ok=0
  if [ $ok_new -ne 0 ]; then
    ok=1; sed "s/^/    new-helper: /" "$SB/${label}.new.err" | head -5 >&2
  elif [ "$expect_old_fail" -eq 1 ] && [ "$ok_old" -eq 0 ]; then
    ok=1; echo "  (old-helper: passed unexpectedly — expected regression)"
  elif [ $ok_old -ne 0 ]; then
    echo "  (old-helper: FAIL)"
  else
    echo "  (old-helper: PASS; behavior already present at HEAD)"
  fi
  check "$label" "$ok"
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
jcfg "$SB/a" | grep -q "\"trunk()\" = \"${BR}@origin\"" || ok=1
[ "$(git -C "$SB/a" config lane.branch)" = "$BR" ] || ok=1
"$HELPER" init "$SB/a" "$LANE_ID" >/dev/null 2>&1 || ok=1
[ -d "$SB/a/.jj" ] || ok=1
check "a init+reinit" "$ok"

# b. pre-existing ::bookmarks() immutable alias survives init.
mkclone b
(cd "$SB/b" && "$JJ" --config 'snapshot.auto-track="none()"' git init --colocate . >/dev/null 2>&1)
cid=$(cat "$SB/b/.jj/repo/config-id")
cat > "$HOME/.config/jj/repos/$cid/config.toml" <<EOF
[revset-aliases]
"trunk()" = "${BR}@origin"
"immutable_heads()" = "builtin_immutable_heads() | ::bookmarks()"
EOF
"$HELPER" init "$SB/b" "$LANE_ID" >/dev/null 2>&1
ok=0
jcfg "$SB/b" | grep -q 'immutable_heads()" = "builtin_immutable_heads() | ::bookmarks()"' || ok=1
jcfg "$SB/b" | grep -q "name = \"$IDENT_NAME\"" || ok=1
check "b keeps-immutable-alias" "$ok"

# c-f. pathspec commit on clone a.
A="$SB/a"
printf 'a-change\n' >> "$A/README.md"          # A: tracked, modified -> commit
printf 'b-change\n' >> "$A/LOG.md"             # B: tracked, modified -> stays
N="NEWFILE-$RANDOM.txt"; echo newfile > "$A/$N"; S="SCRATCH-$$.tmp"; echo scratch > "$A/$S"
out=$("$HELPER" commit "$A" --as "$LANE_ID" -m "selftest c" -- README.md "$N" 2>/dev/null)
CHASH=$(printf '%s\n' "$out" | sed -n 's/^landed //p' | head -1)
ok=0
[ -n "$CHASH" ] || ok=1
names=$(git -C "$A" show --format= --name-only "$CHASH" 2>/dev/null | sort | tr '\n' ' ' | sed 's/ $//')
[ "$names" = "README.md $N" ] || [ "$names" = "$N README.md" ] || ok=1
[ "$(git -C "$A" cat-file -p "$CHASH:README.md" | tail -1)" = "a-change" ] || ok=1
[ "$(git -C "$A" show "$CHASH:LOG.md" | tail -1)" != "b-change" ] || ok=1
[ "$(tail -1 "$A/LOG.md")" = "b-change" ] || ok=1
[ "$(cat "$A/$S")" = "scratch" ] || ok=1
git -C "$A" status --porcelain | grep -q "^?? $S\$" || ok=1
git -C "$A" status --porcelain | grep -q "^ M LOG.md\$" || ok=1
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
[ "$(remote_tip)" = "$CHASH" ] || ok=1
out=$("$HELPER" push "$A" 2>/dev/null)
[ "$(printf '%s\n' "$out" | sed -n 's/^landed //p')" = "$CHASH" ] || ok=1
[ "$(cd "$A" && git rev-list --count "origin/$BR..$BR")" = "0" ] || ok=1
"$HELPER" state "$A" | grep -q 'ahead=0' || ok=1
check "f push-landed" "$ok"

# d2. --as protocol yields protocol-shokunin on author AND committer.
mkclone d2
"$HELPER" init "$SB/d2" "$LANE_ID" >/dev/null 2>&1
echo proto > "$SB/d2/PROTO.md"
out=$("$HELPER" commit "$SB/d2" --as protocol -m "closure" -- PROTO.md 2>/dev/null)
ph=$(printf '%s\n' "$out" | sed -n 's/^landed //p' | head -1)
line=$(git -C "$SB/d2" log -1 --format='%an|%ae|%cn|%ce' "$ph" 2>/dev/null)
if [ "$line" = "protocol-shokunin|protocol@shokunin.local|protocol-shokunin|protocol@shokunin.local" ]; then ok=0; else ok=1; fi
check "d protocol-identity" "$ok"

# g. remote moved by operator -> helper commit+push recovers via fetch+rebase.
op_commit OP-G.md "operator-g"
echo lanework > "$A/LANE-G.md"
out=$("$HELPER" commit "$A" --as "$LANE_ID" -m "selftest g" -- LANE-G.md 2>/dev/null)
PH=$(printf '%s\n' "$out" | sed -n 's/^landed //p' | head -1)
RW=$(printf '%s\n' "$out" | sed -n 's/^rewritten .* -> //p' | head -1)
ok=0
[ -n "$PH" ] || ok=1
remote_log=$(git -C "$REMOTE" log --format='%H %s' "$BR")
printf '%s\n' "$remote_log" | grep -q "$PH" || ok=1
printf '%s\n' "$remote_log" | grep -q 'operator: OP-G.md' || ok=1
op_hash=$(git -C "$REMOTE" log --format=%H -1 --grep='operator: OP-G.md' "$BR")
[ -n "$op_hash" ] && git -C "$REMOTE" merge-base --is-ancestor "$op_hash" "$PH" || ok=1
check "g fetch-rebase-recovery" "$ok"

ok=0
{ [ -n "$RW" ] && [ "$PH" = "$(remote_tip)" ] && git -C "$REMOTE" merge-base --is-ancestor "$RW" "$PH"; } || ok=1
check "g2 rewritten-line" "$ok"

# h. same recovery with the ::bookmarks() immutable alias configured.
B="$SB/b"
echo laneh > "$B/LANE-H.md"
op_commit OP-H.md "operator-h"
out=$("$HELPER" commit "$B" --as "$LANE_ID" -m "selftest h" -- LANE-H.md 2>/dev/null)
PH=$(printf '%s\n' "$out" | sed -n 's/^landed //p' | head -1)
ok=0
[ -n "$PH" ] || ok=1
git -C "$REMOTE" log --format=%H "$BR" | grep -q "$PH" || ok=1
git -C "$REMOTE" log --format=%s "$BR" | grep -q 'operator: OP-H.md' || ok=1
jcfg "$B" | grep -q 'immutable_heads()" = "builtin_immutable_heads() | ::bookmarks()"' || ok=1
check "h immutable-alias-recovery" "$ok"

# j. big untracked files.
mkclone j
head -c 5242880 /dev/urandom > "$SB/j/BIG.bin"
head -c 2097152 /dev/urandom > "$SB/j/MED.bin"
"$HELPER" init "$SB/j" "$LANE_ID" >/dev/null 2>&1
echo jx > "$SB/j/j.md"
out=$("$HELPER" commit "$SB/j" --as "$LANE_ID" -m "selftest j" -- j.md MED.bin 2>/dev/null)
PH=$(printf '%s\n' "$out" | sed -n 's/^landed //p' | head -1)
ok=0
[ -n "$PH" ] || ok=1
"$HELPER" state "$SB/j" >/dev/null 2>&1 || ok=1
git -C "$SB/j" status --porcelain | grep -q '^?? BIG.bin' || ok=1
git -C "$REMOTE" show "$PH:MED.bin" >/dev/null 2>&1 || ok=1
[ "$(git -C "$REMOTE" cat-file -s "$PH:MED.bin")" = "2097152" ] || ok=1
check "j big-files" "$ok"

# k. two lanes write concurrently from the same base: both commits must land.
#    k1/k2 commit locally first (no push), then push in sequence — the second
#    push is lease-rejected, fetches a conflicted bookmark, and must recover.
mkclone k1; mkclone k2
"$HELPER" init "$SB/k1" "$LANE_ID" >/dev/null 2>&1
"$HELPER" init "$SB/k2" "$LANE_ID" >/dev/null 2>&1
echo k1 > "$SB/k1/K1.md"; echo k2 > "$SB/k2/K2.md"
for kl in k1 k2; do
  kf=$(printf '%s' "$kl" | tr '[:lower:]' '[:upper:]')
  ( cd "$SB/$kl" &&
    "$JJ" --config 'snapshot.auto-track="none()"' \
      --config "user.name=$IDENT_NAME" --config "user.email=$IDENT_MAIL" \
      file track --include-ignored -- "root-file:\"$kf.md\"" >/dev/null 2>&1 &&
    "$JJ" --config 'snapshot.auto-track="none()"' \
      --config "user.name=$IDENT_NAME" --config "user.email=$IDENT_MAIL" \
      metaedit --update-author >/dev/null 2>&1 &&
    "$JJ" --config 'snapshot.auto-track="none()"' \
      --config "user.name=$IDENT_NAME" --config "user.email=$IDENT_MAIL" \
      commit -m "$kl" >/dev/null 2>&1 &&
    "$JJ" --ignore-working-copy bookmark set "$BR" -r @- >/dev/null 2>&1 )
done
r1=0; r2=0
"$HELPER" push "$SB/k1" >/dev/null 2>&1 || r1=$?
"$HELPER" push "$SB/k2" >/dev/null 2>&1 || r2=$?
ok=0
[ $r1 -eq 0 ] || ok=1
[ $r2 -eq 0 ] || ok=1
git -C "$REMOTE" show "$BR:K1.md" >/dev/null 2>&1 || ok=1
git -C "$REMOTE" show "$BR:K2.md" >/dev/null 2>&1 || ok=1
(cd "$SB/k2" && "$JJ" --ignore-working-copy bookmark list 2>/dev/null | grep -q 'conflict') && ok=1
(cd "$SB/k2" && "$JJ" --ignore-working-copy log --no-graph -T x -r 'divergent()' 2>/dev/null | grep -q .) && ok=1
check "k concurrent-commits" "$ok"

# l. state changes nothing.
mkclone l
"$HELPER" init "$SB/l" "$LANE_ID" >/dev/null 2>&1
echo dirty >> "$SB/l/README.md"
echo untracked > "$SB/l/u.tmp"
o1=$(cd "$SB/l" && "$JJ" op log --ignore-working-copy -n1 --no-graph -T 'self.id()' 2>/dev/null)
s1=$(git -C "$SB/l" status --porcelain)
"$HELPER" state "$SB/l" >/dev/null 2>&1
o2=$(cd "$SB/l" && "$JJ" op log --ignore-working-copy -n1 --no-graph -T 'self.id()' 2>/dev/null)
s2=$(git -C "$SB/l" status --porcelain)
ok=0
[ "$o1" = "$o2" ] || ok=1
[ "$s1" = "$s2" ] || ok=1
[ -n "$o1" ] || ok=1
check "l state-readonly" "$ok"

# m. git index interplay: a staged entry does not survive a snapshotting
# mutation, but the file content always does.
mkclone m
"$HELPER" init "$SB/m" "$LANE_ID" >/dev/null 2>&1
echo staged-content > "$SB/m/STAGED.md"
git -C "$SB/m" add STAGED.md
"$HELPER" state "$SB/m" >/dev/null 2>&1
echo mfile > "$SB/m/M.md"
out=$("$HELPER" commit "$SB/m" --as "$LANE_ID" -m "selftest m" -- M.md 2>/dev/null)
PH=$(printf '%s\n' "$out" | sed -n 's/^landed //p' | head -1)
staged_after=$(git -C "$SB/m" ls-files --error-unmatch STAGED.md >/dev/null 2>&1 && echo yes || echo no)
echo "  (staged entry after commit: $staged_after)"
ok=0
[ -n "$PH" ] || ok=1
[ -f "$SB/m/STAGED.md" ] && [ "$(cat "$SB/m/STAGED.md")" = "staged-content" ] || ok=1
check "m staged-index-interplay" "$ok"

# n. init on a dirty tree tracks nothing.
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

# o. committing a named directory behaves like `git add <dir>`.
mkclone o
"$HELPER" init "$SB/o" "$LANE_ID" >/dev/null 2>&1
mkdir -p "$SB/o/wave/__pycache__" && echo keep > "$SB/o/wave/keep.md" && echo junk > "$SB/o/wave/__pycache__/x.pyc"
echo '__pycache__/' >> "$SB/o/.git/info/exclude"
out=$("$HELPER" commit "$SB/o" --as "$LANE_ID" -m "selftest o" -- wave 2>/dev/null)
PH=$(printf '%s\n' "$out" | sed -n 's/^landed //p' | head -1)
ok=0
[ -n "$PH" ] || ok=1
git -C "$REMOTE" ls-tree -r --name-only "$PH" -- wave | grep -qx 'wave/keep.md' || ok=1
git -C "$REMOTE" ls-tree -r --name-only "$PH" -- wave | grep -q '__pycache__' && ok=1
check "o dir-commit-skips-ignored" "$ok"

#############################################################################
# z* — hardening cases use fresh sandbox clones. Only the explicitly marked
# regression cases require the HEAD helper to fail; other baseline results are
# diagnostic, and every case checks the current helper's required behavior.

case_z1() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  echo x > "$D/X.md"; "$H" commit "$D" --as testlane -m c1 -- X.md >/dev/null 2>&1 || return 1
  local tip; tip=$(git -C "$REMOTE" rev-parse "refs/heads/$BR")
  git -C "$D" update-ref "refs/heads/$BR" "$BR~1"
  "$H" push "$D" >/dev/null 2>&1 && return 1
  [ "$(git -C "$REMOTE" rev-parse "refs/heads/$BR")" = "$tip" ]
}
try_both z1-backward-push-refused case_z1

case_z1b() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  echo x > "$D/X.md"; "$H" commit "$D" --as testlane -m c1 -- X.md >/dev/null 2>&1 || return 1
  local tip t; tip=$(git -C "$REMOTE" rev-parse "refs/heads/$BR")
  t=$(git -C "$D" -c user.name=operator -c user.email=op@sandbox.local commit-tree "$BR^{tree}" -p "$BR~1" -m sideways)
  git -C "$D" update-ref "refs/heads/$BR" "$t"
  "$H" push "$D" >/dev/null 2>&1 && return 1
  [ "$(git -C "$REMOTE" rev-parse "refs/heads/$BR")" = "$tip" ]
}
try_both z1b-sideways-push-refused case_z1b

case_z2() {
  git -C "$D" config user.name op; git -C "$D" config user.email op@x
  echo local > "$D/LOCAL.md"; git -C "$D" add LOCAL.md; git -C "$D" commit -qm "local work"
  local d="$SB/op2-$RANDOM"; git clone -q "$REMOTE" "$d"
  git -C "$d" config user.name op; git -C "$d" config user.email op@x
  echo rem > "$d/REM.md"; git -C "$d" add REM.md; git -C "$d" commit -qm "operator"; git -C "$d" push -q origin "HEAD:$BR"
  git -C "$D" fetch -q origin
  "$H" init "$D" testlane >/dev/null 2>&1 && return 1
  git -C "$REMOTE" merge-base --is-ancestor "$(git -C "$d" rev-parse HEAD)" "$BR"
}
try_both z2-init-diverged-refused case_z2

case_z3() {
  git -C "$D" checkout -qb feat
  git -C "$D" push -q origin feat:feat
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  echo f1 > "$D/F1.md"; "$H" commit "$D" --as testlane -m f1 -- F1.md >/dev/null 2>&1 || return 1
  [ "$("$H" state "$D" | sed -n 's/^state branch=\([^ ]*\).*/\1/p')" = "feat" ] || return 1
  echo f2 > "$D/F2.md"; "$H" commit "$D" --as testlane -m f2 -- F2.md >/dev/null 2>&1 || return 1
  git -C "$REMOTE" rev-parse --verify -q refs/heads/feat >/dev/null || return 1
  git -C "$REMOTE" cat-file -e feat:F2.md
}
try_both z3-branch-binding case_z3

case_z4() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  mkdir -p "$D/.ufo/state"; echo s > "$D/.ufo/state/run.json"; echo n > "$D/.ufo/notes.md"
  local base
  base=$(git -C "$REMOTE" ls-tree -r --name-only "$BR" -- .ufo | sort)
  "$H" commit "$D" --as testlane -m x -- ./ >/dev/null 2>&1 && return 1
  "$H" commit "$D" --as testlane -m x -- .ufo >/dev/null 2>&1 && return 1
  "$H" commit "$D" --as testlane -m x -- .ufo/state >/dev/null 2>&1 && return 1
  "$H" commit "$D" --as testlane -m x -- ./.ufo/state/run.json >/dev/null 2>&1 && return 1
  ! git -C "$REMOTE" cat-file -e "$BR:.ufo/state/run.json" 2>/dev/null || return 1
  [ "$(git -C "$REMOTE" ls-tree -r --name-only "$BR" -- .ufo | sort)" = "$base" ]
}
try_both z4-ufo-paths-refused case_z4

case_z5() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  echo a > "$D/a~b.md"; echo x > "$D/x|y.md"; echo s > "$D/sp ace.md"
  local out ph
  out=$("$H" commit "$D" --as testlane -m names -- "a~b.md" "x|y.md" "sp ace.md" 2>/dev/null)
  ph=$(printf '%s\n' "$out" | sed -n 's/^landed //p')
  [ -n "$ph" ] || return 1
  git -C "$REMOTE" cat-file -e "$BR:a~b.md" &&
  git -C "$REMOTE" cat-file -e "$BR:x|y.md" &&
  git -C "$REMOTE" cat-file -e "$BR:sp ace.md"
}
try_both z5-fileset-literals case_z5

case_z6() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  head -c 11534336 /dev/urandom > "$D/BIG.bin"
  "$H" commit "$D" --as testlane -m big -- BIG.bin >/dev/null 2>&1 && return 1
  ! git -C "$REMOTE" cat-file -e "$BR:BIG.bin" 2>/dev/null
}
try_both z6-large-file-gate case_z6

case_z7() {
  mkdir -p "$D/tests/vadv54-run/p/p6repo/.git" "$D/tests/vadv54-run/p/p6repo/inner"
  echo one > "$D/tests/vadv54-run/p/p6repo/one.txt"; echo keep > "$D/tests/vadv54-run/p/p6repo/inner/keep.txt"
  git -C "$D" add tests && git -C "$D" -c user.name=seed -c user.email=s@x commit -qm "add tests" \
    && git -C "$D" push -q origin "HEAD:$BR" || return 1
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  "$H" commit "$D" --as testlane -m tests -- tests/vadv54-run >/dev/null 2>&1 && return 1
  git -C "$REMOTE" cat-file -e "$BR:tests/vadv54-run/p/p6repo/one.txt"
}
try_both z7-phantom-deletion case_z7

case_z8() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  local key holder before elapsed
  key=$(printf '%s' "$(cd "$D" && pwd -P)" | tr '/.' '__' | tr -cd '[:alnum:]_-')
  flock -w2 "$HYAKU_STATE/jj-$key.lock" true || return 1
  ( exec {fd}>"$HYAKU_STATE/jj-$key.lock"; flock -n "$fd" || exit 1; sleep 3 ) &
  holder=$!; sleep 1
  before=$(date +%s)
  ( cd "$D" && echo r > rel.md && timeout 12 "$H" commit . --as testlane -m rel -- rel.md ) >/dev/null 2>&1
  elapsed=$(( $(date +%s) - before ))
  wait "$holder" 2>/dev/null || true
  [ "$elapsed" -ge 2 ] || return 1
  echo a > "$D/abs.md"; timeout 30 "$H" commit "$D" --as testlane -m abs -- abs.md >/dev/null 2>&1
}
try_both z8-lock-canonical case_z8

case_z9() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  local d="$SB/opz9-$RANDOM" out ph
  git clone -q "$REMOTE" "$d"
  git -C "$d" config user.name op; git -C "$d" config user.email op@x
  echo op > "$d/OPZ.md"; git -C "$d" add OPZ.md; git -C "$d" commit -qm op; git -C "$d" push -q origin "HEAD:$BR"
  echo c > "$D/C.md"
  out=$("$H" commit "$D" --as protocol -m closure -- C.md 2>/dev/null)
  ph=$(printf '%s\n' "$out" | sed -n 's/^landed //p'); [ -n "$ph" ] || return 1
  [ "$(git -C "$REMOTE" log -1 --format='%an|%ae|%cn|%ce' "$ph")" = \
    "protocol-shokunin|protocol@shokunin.local|protocol-shokunin|protocol@shokunin.local" ]
}
try_both z9-protocol-committer-recovery case_z9

case_z10() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  local out ph
  mv "$REMOTE" "$REMOTE.off"
  echo w1 > "$D/W1.md"
  if "$H" commit "$D" --as testlane -m w1 -- W1.md >/dev/null 2>&1; then
    mv "$REMOTE.off" "$REMOTE"; return 1
  fi
  mv "$REMOTE.off" "$REMOTE"
  "$H" push "$D" >/dev/null 2>&1 || return 1
  echo w2 > "$D/W2.md"
  out=$("$H" commit "$D" --as testlane -m w2 -- W2.md 2>/dev/null)
  ph=$(printf '%s\n' "$out" | sed -n 's/^landed //p'); [ -n "$ph" ] || return 1
  git -C "$REMOTE" cat-file -e "$BR:W2.md"
}
try_both z10-retry-lands case_z10

case_z11() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  local cited d
  echo c > "$D/CITED.md"; "$H" commit "$D" --as testlane -m cited -- CITED.md >/dev/null 2>&1 || return 1
  cited=$(git -C "$REMOTE" rev-parse "$BR")
  d="$SB/opz11-$RANDOM"; git clone -q "$REMOTE" "$d"
  git -C "$d" config user.name op; git -C "$d" config user.email op@x
  git -C "$d" reset -q --hard HEAD~1; echo z > "$d/Z.md"; git -C "$d" add Z.md
  git -C "$d" commit -qm rewrite; git -C "$d" push -qf origin "HEAD:$BR"
  echo n > "$D/N.md"
  "$H" commit "$D" --as testlane -m next -- N.md >/dev/null 2>&1 && return 1
  "$H" push "$D" >/dev/null 2>&1 && return 1
  ! git -C "$REMOTE" merge-base --is-ancestor "$cited" "$BR" 2>/dev/null || return 1
  ! git -C "$REMOTE" log --format=%s "$BR" | grep -q cited
}
try_both z11-remote-rewrite-refused case_z11

case_z12() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  printf 'seat-half-line\n' >> "$D/README.md"
  ( cd "$D" && "$JJ" --config "user.name=testlane-shokunin" --config "user.email=testlane@shokunin.local" \
      commit -m "seat wip checkpoint" >/dev/null 2>&1 )
  echo real > "$D/REAL.md"
  "$H" commit "$D" --as testlane -m real -- REAL.md >/dev/null 2>&1 || true
  ! git -C "$REMOTE" log --format=%s "$BR" | grep -q "seat wip" || return 1
  ! git -C "$REMOTE" show "$BR:README.md" | tail -1 | grep -qx "seat-half-line"
}
try_both z12-seat-commit-not-swept case_z12

case_z13() {
  git -C "$D" config user.name ci; git -C "$D" config user.email ci@local
  echo raw > "$D/RAW.md"; git -C "$D" add RAW.md; git -C "$D" commit -qm "raw git commit"
  local raw; raw=$(git -C "$D" rev-parse HEAD)
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  echo mine > "$D/MINE.md"
  "$H" commit "$D" --as testlane -m mine -- MINE.md >/dev/null 2>&1 && return 1
  "$H" push "$D" >/dev/null 2>&1 && return 1
  ! git -C "$REMOTE" merge-base --is-ancestor "$raw" "$BR" 2>/dev/null
}
try_both z13-foreign-identity-refused case_z13

case_z14() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  echo x > "$D/X.md"
  "$H" commit "$D" --as testlane -m x -- X.md >/dev/null 2>&1 || return 1
  echo y > "$D/Y.md"
  "$H" commit "$D" --as kama -m x -- Y.md >/dev/null 2>&1 && return 1
  ! git -C "$REMOTE" cat-file -e "$BR:Y.md" 2>/dev/null
}
try_both z14-foreign-as-refused case_z14

case_z15() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  local wt="$SB/wt-$RANDOM"
  git -C "$D" worktree add -q --detach "$wt" "$BR" 2>/dev/null || return 1
  "$H" init "$wt" testlane >/dev/null 2>&1 && return 1
  "$H" commit "$wt" --as testlane -m x -- README.md >/dev/null 2>&1 && return 1
  "$H" state "$wt" >/dev/null 2>&1 && return 1
  return 0
}
try_both z15-worktree-refused case_z15

case_z16() {
  export JJ_USER="Env Attacker" JJ_EMAIL=env@evil.test
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  echo x > "$D/X.md"
  local out ph
  out=$("$H" commit "$D" --as testlane -m env -- X.md 2>/dev/null)
  ph=$(printf '%s\n' "$out" | sed -n 's/^landed //p'); [ -n "$ph" ] || return 1
  [ "$(git -C "$REMOTE" log -1 --format='%an|%ae|%cn|%ce' "$ph")" = \
    "testlane-shokunin|testlane@shokunin.local|testlane-shokunin|testlane@shokunin.local" ]
}
try_both z16-env-scrub case_z16

jj_lane_commit() { # <file> <msg> — native jj commit inside $D, lane identity
  ( cd "$D" &&
    "$JJ" --config 'snapshot.auto-track="none()"' \
      --config "user.name=testlane-shokunin" --config "user.email=testlane@shokunin.local" \
      file track --include-ignored -- "$1" >/dev/null 2>&1 &&
    "$JJ" --config 'snapshot.auto-track="none()"' \
      --config "user.name=testlane-shokunin" --config "user.email=testlane@shokunin.local" \
      metaedit --update-author >/dev/null 2>&1 &&
    "$JJ" --config 'snapshot.auto-track="none()"' \
      --config "user.name=testlane-shokunin" --config "user.email=testlane@shokunin.local" \
      commit -m "$2" -- "$1" >/dev/null 2>&1 &&
    "$JJ" --ignore-working-copy bookmark set "$BR" -r @- >/dev/null 2>&1 )
}

jj_strand_commit() { # <file> <msg> [identity] — commit without moving the bookmark
  local file=$1 msg=$2 who=${3:-testlane}
  ( cd "$D" &&
    "$JJ" --config 'snapshot.auto-track="none()"' \
      --config "user.name=${who}-shokunin" --config "user.email=${who}@shokunin.local" \
      file track --include-ignored -- "root-file:\"$file\"" >/dev/null 2>&1 &&
    "$JJ" --config 'snapshot.auto-track="none()"' \
      --config "user.name=${who}-shokunin" --config "user.email=${who}@shokunin.local" \
      metaedit --update-author >/dev/null 2>&1 &&
    "$JJ" --config 'snapshot.auto-track="none()"' \
      --config "user.name=${who}-shokunin" --config "user.email=${who}@shokunin.local" \
      commit -m "$msg" -- "$file" >/dev/null 2>&1 )
}


jj_stranded_hash() {
  ( cd "$D" && "$JJ" --ignore-working-copy log --no-graph -r '@-' -T commit_id 2>/dev/null )
}
INCIDENT_SRC=.ufo/waves/round-20/isolate.sh
INCIDENT_DST=.ufo/waves/round-20/w2/IsoV3/isolate.sh
seed_incident_source() {
  mkdir -p "$D/.ufo/waves/round-20" || return 1
  printf 'incident source bytes\n' > "$D/$INCIDENT_SRC"
  "$H" commit "$D" --as testlane -m incident-source -- "$INCIDENT_SRC" >/dev/null 2>&1
}


case_z17() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  echo local > "$D/LC.md"
  jj_lane_commit LC.md "lane commit" || return 1
  local d="$SB/opz17-$RANDOM" tip
  git clone -q "$REMOTE" "$d"
  git -C "$d" config user.name op; git -C "$d" config user.email op@x
  echo op > "$d/OPZ17.md"; git -C "$d" add OPZ17.md; git -C "$d" commit -qm op; git -C "$d" push -q origin "HEAD:$BR"
  ( cd "$D" && "$JJ" --ignore-working-copy git fetch --remote origin >/dev/null 2>&1 )
  tip=$(git -C "$REMOTE" rev-parse "refs/heads/$BR")
  "$H" push "$D" >/dev/null 2>&1 && return 1
  [ "$(git -C "$REMOTE" rev-parse "refs/heads/$BR")" = "$tip" ]
}
try_both z17-conflicted-bookmark case_z17

case_z18() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  echo l > "$D/L.md"; "$H" commit "$D" --as testlane -m l -- L.md >/dev/null 2>&1 || return 1
  local d="$SB/opz18-$RANDOM" tip out ph
  git clone -q "$REMOTE" "$d"
  git -C "$d" config user.name op; git -C "$d" config user.email op@x
  echo op > "$d/OPZ18.md"; git -C "$d" add OPZ18.md; git -C "$d" commit -qm op; git -C "$d" push -q origin "HEAD:$BR"
  echo l2 > "$D/L2.md"
  jj_lane_commit L2.md "l2" || return 1
  tip=$(git -C "$REMOTE" rev-parse "refs/heads/$BR")
  "$H" push --no-rebase "$D" >/dev/null 2>&1 && return 1
  [ "$(git -C "$REMOTE" rev-parse "refs/heads/$BR")" = "$tip" ] || return 1
  out=$("$H" push "$D" 2>/dev/null)
  ph=$(printf '%s\n' "$out" | sed -n 's/^landed //p'); [ -n "$ph" ]
}
try_both z18-norebase-driver-push case_z18

case_z19() {
  ( cd "$D" && "$JJ" git init --colocate . >/dev/null 2>&1 )
  echo scratch > "$D/SCRATCH-LEGACY.md"
  ( cd "$D" && "$JJ" status >/dev/null 2>&1 )
  "$H" init "$D" testlane >"$D/.initout" 2>&1 || return 1
  grep -q "untracked (kept on disk): SCRATCH-LEGACY.md" "$D/.initout" || return 1
  [ -f "$D/SCRATCH-LEGACY.md" ] || return 1
  git -C "$D" status --porcelain | grep -q "^?? SCRATCH-LEGACY.md" || return 1
  ! ( cd "$D" && "$JJ" --ignore-working-copy file list -r @ | grep -q "SCRATCH-LEGACY" )
}
try_both z19-legacy-untracks-scratch case_z19

case_z20() {
  ( cd "$D" && "$JJ" --config 'snapshot.auto-track="none()"' git init --colocate . >/dev/null 2>&1 )
  git -C "$D" config user.name testlane-shokunin; git -C "$D" config user.email testlane@shokunin.local
  echo g1 > "$D/G1.md"; git -C "$D" add G1.md; git -C "$D" commit -qm "git commit one"
  echo g2 > "$D/G2.md"; git -C "$D" add G2.md; git -C "$D" commit -qm "git commit two"
  local before
  before=$(git -C "$D" status --porcelain --untracked-files=no)
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  [ "$(git -C "$D" status --porcelain --untracked-files=no)" = "$before" ] || return 1
  [ "$(cd "$D" && "$JJ" --ignore-working-copy log --no-graph -r @- -T commit_id)" = \
    "$(git -C "$D" rev-parse "refs/heads/$BR")" ]
}
try_both z20-stale-jj-imports-head case_z20

case_z21() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  local out rc
  out=$("$H" commit "$D" --as testlane -m noop -- README.md 2>/dev/null); rc=$?
  [ $rc -eq 0 ] || return 1
  printf '%s\n' "$out" | grep -q "^nothing to commit" || return 1
  ! printf '%s\n' "$out" | grep -qE "[0-9a-f]{40}|landed|pushed|committed"
}
try_both z21-nothing-no-hash case_z21

case_z22() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  echo x > "$D/X.md"
  local holder out rc
  ( exec {fd}>"$D/.git/index.lock"; flock -n "$fd" || exit 1; sleep 4 ) &
  holder=$!; sleep 1
  out=$("$H" commit "$D" --as testlane -m x -- X.md 2>/dev/null); rc=$?
  wait "$holder" 2>/dev/null || true
  [ $rc -ne 0 ] || return 1
  ! printf '%s\n' "$out" | grep -q "nothing to commit"
}
try_both z22-index-lock-error case_z22

case_z23() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  git -C "$D" rm -q README.md
  local out ph
  out=$("$H" commit "$D" --as testlane -m del -- README.md 2>/dev/null)
  ph=$(printf '%s\n' "$out" | sed -n 's/^landed //p'); [ -n "$ph" ] || return 1
  ! git -C "$REMOTE" cat-file -e "$BR:README.md" 2>/dev/null
}
try_both z23-deletion-lands case_z23

case_z24() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  mv "$D/LOG.md" "$D/RENAMED.md"
  local out ph
  out=$("$H" commit "$D" --as testlane -m mv -- LOG.md RENAMED.md 2>/dev/null)
  ph=$(printf '%s\n' "$out" | sed -n 's/^landed //p'); [ -n "$ph" ] || return 1
  ! git -C "$REMOTE" cat-file -e "$BR:LOG.md" 2>/dev/null || return 1
  git -C "$REMOTE" cat-file -e "$BR:RENAMED.md"
}
try_both z24-rename-lands case_z24

# z25 — first colocation refuses a repo with staged index entries (jj init
# would silently unstage them). The staged entry must survive the refusal.
case_z25() {
  echo s > "$D/STAGED-INIT.md"
  git -C "$D" add STAGED-INIT.md
  "$H" init "$D" testlane >/dev/null 2>&1 && return 1
  [ ! -d "$D/.jj" ] || return 1
  git -C "$D" ls-files --error-unmatch -- STAGED-INIT.md >/dev/null 2>&1
}
try_both z25-init-staged-refused case_z25

# z26 — commit refuses when the repo lost snapshot.auto-track="none()"
# ("run init"): an unguarded snapshot would track every untracked file.
case_z26() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  ( cd "$D" && "$JJ" --ignore-working-copy config unset --repo snapshot.auto-track >/dev/null 2>&1 ) || return 1
  echo x > "$D/X.md"
  "$H" commit "$D" --as testlane -m x -- X.md >/dev/null 2>&1 && return 1
  ! git -C "$REMOTE" cat-file -e "$BR:X.md" 2>/dev/null
}
try_both z26-commit-needs-init-config case_z26

# z27 — state is pure git and refuses a non-40-hex (missing) origin ref.
case_z27() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  git -C "$D" update-ref -d "refs/remotes/origin/$BR"
  "$H" state "$D" >/dev/null 2>&1 && return 1
  "$H" state "$D" 2>&1 | grep -q "not a 40-hex"
}
try_both z27-state-needs-40hex case_z27


# z28–z30 — machine-readable tree paths keep nested move/copy summaries out
# of the scope guard; an unchanged copy source is not a changed path.
case_z28() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  seed_incident_source || return 1
  mkdir -p "$D/.ufo/waves/round-20/w2/IsoV3"
  mv "$D/$INCIDENT_SRC" "$D/$INCIDENT_DST"
  local out ph
  out=$("$H" commit "$D" --as testlane -m move-in -- "$INCIDENT_SRC" "$INCIDENT_DST" 2>/dev/null)
  ph=$(printf '%s\n' "$out" | sed -n 's/^landed //p' | head -1)
  [ -n "$ph" ] || return 1
  ! git -C "$REMOTE" cat-file -e "$BR:$INCIDENT_SRC" 2>/dev/null || return 1
  git -C "$REMOTE" cat-file -e "$BR:$INCIDENT_DST"
}
try_both z28-incident-move-into-nested case_z28 1

case_z29() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  mkdir -p "$D/.ufo/waves/round-20/w2/IsoV3"
  printf 'outgoing isolate bytes\n' > "$D/$INCIDENT_DST"
  "$H" commit "$D" --as testlane -m seed -- "$INCIDENT_DST" >/dev/null 2>&1 || return 1
  mv "$D/$INCIDENT_DST" "$D/$INCIDENT_SRC"
  local out ph
  out=$("$H" commit "$D" --as testlane -m move-out -- "$INCIDENT_DST" "$INCIDENT_SRC" 2>/dev/null)
  ph=$(printf '%s\n' "$out" | sed -n 's/^landed //p' | head -1)
  [ -n "$ph" ] || return 1
  ! git -C "$REMOTE" cat-file -e "$BR:$INCIDENT_DST" 2>/dev/null || return 1
  git -C "$REMOTE" cat-file -e "$BR:$INCIDENT_SRC"
}
try_both z29-incident-move-out-of-nested case_z29 1

case_z30() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  seed_incident_source || return 1
  mkdir -p "$D/.ufo/waves/round-20/w2/IsoV3"
  cp "$D/$INCIDENT_SRC" "$D/$INCIDENT_DST"
  local before out ph
  before=$(git -C "$D" show "$BR:$INCIDENT_SRC" | sha256sum)
  out=$("$H" commit "$D" --as testlane -m copy -- "$INCIDENT_DST" 2>/dev/null)
  ph=$(printf '%s\n' "$out" | sed -n 's/^landed //p' | head -1)
  [ -n "$ph" ] || return 1
  [ "$(git -C "$REMOTE" show "$BR:$INCIDENT_SRC" | sha256sum)" = "$before" ] || return 1
  [ "$(git -C "$REMOTE" show "$BR:$INCIDENT_DST" | sha256sum)" = "$before" ]
}
try_both z30-incident-copy-destination-only case_z30
reject_recovery() { # <candidate> <identity> <expected-error> <requested-path>...
  local candidate=$1 id=$2 expected=$3 before after remote_before remote_after rc
  local wc_before wc_after status_before status_after
  shift 3
  before=$(git -C "$D" rev-parse "refs/heads/$BR") || return 1
  remote_before=$(remote_tip) || return 1
  wc_before=$(cd "$D" && "$JJ" --ignore-working-copy log --no-graph -r @ -T commit_id 2>/dev/null) || return 1
  status_before=$(git -C "$D" status --porcelain --untracked-files=all 2>/dev/null) || return 1
  "$H" recover "$D" --as "$id" --revision "$candidate" -- "$@" >"$SB/recover.err" 2>&1
  rc=$?
  [ "$rc" -eq 1 ] || return 1
  grep -Fq -- "$expected" "$SB/recover.err" || return 1
  after=$(git -C "$D" rev-parse "refs/heads/$BR") || return 1
  remote_after=$(remote_tip) || return 1
  wc_after=$(cd "$D" && "$JJ" --ignore-working-copy log --no-graph -r @ -T commit_id 2>/dev/null) || return 1
  status_after=$(git -C "$D" status --porcelain --untracked-files=all 2>/dev/null) || return 1
  [ "$after" = "$before" ] && [ "$remote_after" = "$remote_before" ] \
    && [ "$wc_after" = "$wc_before" ] && [ "$status_after" = "$status_before" ]
}

case_z31() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  seed_incident_source || return 1
  mkdir -p "$D/.ufo/waves/round-20/w2/IsoV3"
  mv "$D/$INCIDENT_SRC" "$D/$INCIDENT_DST"
  ( cd "$D" &&
    "$JJ" --config 'snapshot.auto-track="none()"' \
      --config "user.name=$IDENT_NAME" --config "user.email=$IDENT_MAIL" \
      file track --include-ignored -- "root-file:\"$INCIDENT_DST\"" >/dev/null 2>&1 &&
    "$JJ" --config 'snapshot.auto-track="none()"' \
      --config "user.name=$IDENT_NAME" --config "user.email=$IDENT_MAIL" \
      metaedit --update-author >/dev/null 2>&1 &&
    "$JJ" --config 'snapshot.auto-track="none()"' \
      --config "user.name=$IDENT_NAME" --config "user.email=$IDENT_MAIL" \
      commit -m rename-stranded >/dev/null 2>&1 ) || return 1
  local candidate
  candidate=$(jj_stranded_hash)
  [ -n "$candidate" ] || return 1
  reject_recovery "$candidate" testlane "commit changed a path outside the request" "$INCIDENT_DST"
}
try_both z31-rename-unrequested-source-refused case_z31

case_z32() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  echo stranded > "$D/RECOVERED.md"
  jj_strand_commit RECOVERED.md stranded || return 1
  local branch_before candidate out ph wc_before wc_after
  branch_before=$(git -C "$D" rev-parse "refs/heads/$BR") || return 1
  candidate=$(jj_stranded_hash)
  [ -n "$candidate" ] || return 1
  [ "$(git -C "$D" rev-parse "$candidate^")" = "$branch_before" ] || return 1
  printf 'report edit\n' >> "$D/README.md"
  printf 'untracked report\n' > "$D/UNRELATED-REPORT.md"
  cp "$D/README.md" "$SB/z32-readme.before"
  cp "$D/UNRELATED-REPORT.md" "$SB/z32-report.before"
  wc_before=$(cd "$D" && "$JJ" --ignore-working-copy log --no-graph -r @ -T commit_id 2>/dev/null)
  out=$("$H" recover "$D" --as testlane --revision "$candidate" -- RECOVERED.md 2>/dev/null)
  ph=$(printf '%s\n' "$out" | sed -n 's/^landed //p' | head -1)
  [ "$ph" = "$candidate" ] || return 1
  [ "$(git -C "$D" rev-parse "refs/heads/$BR")" = "$candidate" ] || return 1
  [ "$(remote_tip)" = "$candidate" ] || return 1
  git -C "$REMOTE" cat-file -e "$BR:RECOVERED.md" || return 1
  cmp -s "$SB/z32-readme.before" "$D/README.md" || return 1
  cmp -s "$SB/z32-report.before" "$D/UNRELATED-REPORT.md" || return 1
  wc_after=$(cd "$D" && "$JJ" --ignore-working-copy log --no-graph -r @ -T commit_id 2>/dev/null)
  [ "$wc_after" = "$wc_before" ] || return 1
  [ "$(cd "$D" && "$JJ" --ignore-working-copy log --no-graph -r @- -T commit_id 2>/dev/null)" = "$candidate" ]
}
try_both z32-explicit-recovery-preserves-working-copy case_z32 1

case_z33() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  echo first > "$D/FIRST.md"
  jj_strand_commit FIRST.md first || return 1
  echo second > "$D/SECOND.md"
  jj_strand_commit SECOND.md second || return 1
  local candidate
  candidate=$(jj_stranded_hash)
  [ -n "$candidate" ] || return 1
  reject_recovery "$candidate" testlane "candidate is not a single-parent child" SECOND.md
}
try_both z33-wrong-parent-refused case_z33

case_z34() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  echo wrong > "$D/WRONG-IDENTITY.md"
  jj_strand_commit WRONG-IDENTITY.md wrong-identity other || return 1
  local candidate
  candidate=$(jj_stranded_hash)
  [ -n "$candidate" ] || return 1
  reject_recovery "$candidate" testlane "candidate identity does not match requested" WRONG-IDENTITY.md
}
try_both z34-wrong-identity-refused case_z34

case_z35() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  echo first > "$D/FIRST-CANDIDATE.md"
  jj_strand_commit FIRST-CANDIDATE.md first || return 1
  local first tip
  first=$(jj_stranded_hash)
  tip=$(git -C "$D" rev-parse "refs/heads/$BR") || return 1
  ( cd "$D" && "$JJ" --config 'snapshot.auto-track="none()"' new "$tip" >/dev/null 2>&1 ) || return 1
  echo second > "$D/SECOND-CANDIDATE.md"
  jj_strand_commit SECOND-CANDIDATE.md second || return 1
  [ -n "$first" ] || return 1
  reject_recovery "$first" testlane "candidate is not the direct parent of the current working copy" FIRST-CANDIDATE.md
}
try_both z35-not-current-candidate-refused case_z35

case_z36() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  local base left right candidate
  base=$(git -C "$D" rev-parse "refs/heads/$BR") || return 1
  echo left > "$D/CONFLICT.md"
  jj_strand_commit CONFLICT.md left || return 1
  left=$(jj_stranded_hash)
  ( cd "$D" && "$JJ" --config 'snapshot.auto-track="none()"' new "$base" >/dev/null 2>&1 ) || return 1
  echo right > "$D/CONFLICT.md"
  jj_strand_commit CONFLICT.md right || return 1
  right=$(jj_stranded_hash)
  [ -n "$left" ] && [ -n "$right" ] || return 1
  ( cd "$D" && "$JJ" --ignore-working-copy bookmark set "$BR" -r "$left" >/dev/null 2>&1 &&
    "$JJ" --config 'snapshot.auto-track="none()"' new "$left" "$right" >/dev/null 2>&1 &&
    "$JJ" --config 'snapshot.auto-track="none()"' \
      --config "user.name=$IDENT_NAME" --config "user.email=$IDENT_MAIL" \
      metaedit --update-author >/dev/null 2>&1 &&
    "$JJ" --config 'snapshot.auto-track="none()"' \
      --config "user.name=$IDENT_NAME" --config "user.email=$IDENT_MAIL" \
      commit -m conflicted-stranded >/dev/null 2>&1 ) || return 1
  candidate=$(jj_stranded_hash)
  [ -n "$candidate" ] || return 1
  reject_recovery "$candidate" testlane "has unresolved conflicts" CONFLICT.md
}
try_both z36-conflicted-candidate-refused case_z36

case_z37() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  echo actual > "$D/ACTUAL.md"
  jj_strand_commit ACTUAL.md out-of-scope || return 1
  local candidate
  candidate=$(jj_stranded_hash)
  [ -n "$candidate" ] || return 1
  reject_recovery "$candidate" testlane "commit changed a path outside the request" README.md
}
try_both z37-out-of-scope-refused case_z37

case_z38() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  mkdir -p "$D/.ufo/state"
  echo private > "$D/.ufo/state/run.json"
  jj_strand_commit .ufo/state/run.json state || return 1
  local candidate
  candidate=$(jj_stranded_hash)
  [ -n "$candidate" ] || return 1
  reject_recovery "$candidate" testlane "driver runtime is never committed by a lane" README.md
}
try_both z38-state-path-refused case_z38
case_z39() {
  "$H" init "$D" testlane >/dev/null 2>&1 || return 1
  local tip candidate
  tip=$(git -C "$D" rev-parse "refs/heads/$BR") || return 1
  ( cd "$D" && "$JJ" --config 'snapshot.auto-track="none()"' \
      --config "user.name=$IDENT_NAME" --config "user.email=$IDENT_MAIL" \
      new "$tip" >/dev/null 2>&1 ) || return 1
  candidate=$(cd "$D" && "$JJ" --ignore-working-copy log --no-graph -r @ -T commit_id 2>/dev/null)
  [ -n "$candidate" ] || return 1
  ( cd "$D" && "$JJ" --config 'snapshot.auto-track="none()"' new "$candidate" >/dev/null 2>&1 ) || return 1
  reject_recovery "$candidate" testlane "has no changed paths" README.md
}
try_both z39-empty-candidate-refused case_z39

# p. `state` serves the driver for EVERY lane: a plain git clone never init'ed
# (detached HEAD) and a lane colocated before lane.branch existed must still
# report their branch. New helper only — the old helper also detects branches.
mkclone p
git -C "$SB/p" checkout -q --detach
ok=0
"$HELPER" state "$SB/p" 2>/dev/null | grep -q "^state branch=$BR " || ok=1
"$HELPER" init "$SB/p" "$LANE_ID" >/dev/null 2>&1 || ok=1
git -C "$SB/p" config --unset lane.branch
"$HELPER" state "$SB/p" 2>/dev/null | grep -q "^state branch=$BR " || ok=1
check "p state-without-lane-branch" "$ok"

echo "selftest $pass/$total"
[ "$pass" -eq "$total" ]
