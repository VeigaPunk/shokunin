# JjDocIdentity — author/committer identity, precedence, rebase semantics and signing (jj 0.45.1)

**Verdict.** In jj 0.45.1 an identity is resolved from a fixed ladder:
built-in defaults → system config → base env → **user config → repo config → workspace config** →
**`JJ_USER`/`JJ_EMAIL` (override-env layer)** → **`--config` / `--config-file` (command line)**.
The resolved identity is stamped as **both author and committer** on a new commit. Every rewrite
(`rebase`, `describe`, `squash`, `metaedit`, even `jj sign`) replaces the **committer** with the
identity resolved *at that moment* and leaves the **author name/email/timestamp** untouched, with
two documented code-level exceptions (empty-author backfill, discardable-commit author-date reset).
Signing on rewrite is decided by `signing.behavior` against the commit's **author email**:
`keep` re-signs only commits that were already signed *and* authored by the current user, `own`
signs commits authored by the current user, `force` signs everything, `drop` removes the signature;
anything not covered loses its signature. Signing failures are hard errors (exit 255), not warnings.

- Toolchain: `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`, `git version 2.56.0`,
  `ssh-keygen` and `gpg` from the host. Nothing was installed or upgraded for this report.
- Docs: versioned **v0.45.1** pages under `https://docs.jj-vcs.dev/v0.45.1/…`; the binary's own
  `jj help -k config` repeats the precedence sentence and file-location notes quoted below. The
  site's `latest` alias is
  **v0.46.0** (`https://docs.jj-vcs.dev/versions.json` → `{"version":"v0.46.0","aliases":["latest"]}`);
  `https://jj-vcs.github.io/jj/latest/…` 301-redirects to `https://docs.jj-vcs.dev/latest/…`.
  The 0.45.0/0.45.1 CHANGELOG sections contain no author/committer/precedence change; the only
  signing entry is a storage fix (“Signatures on commits in SHA-256 Git repositories are now stored
  under the `gpgsig-sha256` header”, 0.45.1).
- Sandbox: all probes ran in `/fast/scratch/jj-wave/JjDocIdentity/` (fresh `git init` +
  `jj git init --colocate` per experiment); every `origin` was a sandbox bare repo. No live repo
  was written, staged, fetched, checked out or pushed (the only live-tree write is this report
  file), and no `jj` command was run with a working directory or `-R` inside
  `/home/vgpnk/Projects/shokunin`. Experiment scripts (`expA.sh` … `expE3.sh`) plus the inline
  sandboxes `expF`–`expL2` and the cited failure states are kept there; that sandbox is retained
  because this report cites those failures (see F3.1).
- In transcripts, `$S` = `/fast/scratch/jj-wave/JjDocIdentity`, `…` marks trimmed output only
  where stated, and `JJ_CONFIG` points at a sandbox TOML file so the host's real user config is
  never loaded.

---

## F1 — Identity sources and precedence

**Citations.**

- v0.45.1 config → “Config files and TOML”:
  <https://docs.jj-vcs.dev/v0.45.1/config/#config-files-and-toml> —
  > settings from earlier items in the list are overridden by the settings from later items if they disagree

  (20 words). The list immediately above that sentence is: built-in, user, repo, workspace,
  command-line. `jj help -k config` prints the same list and the same sentence.
- v0.45.1 config → “Specifying config on the command-line”:
  <https://docs.jj-vcs.dev/v0.45.1/config/#specifying-config-on-the-command-line> —
  > This overrides settings defined in config files or environment variables.

  (10 words.)
- v0.45.1 config → “User config files”:
  <https://docs.jj-vcs.dev/v0.45.1/config/#user-config-files> —
  > this variable only affects user-level and system-level config files; repo and workspace configs are unaffected

  (16 words, about `JJ_CONFIG`). This is why every experiment below could isolate user config in a
  sandbox TOML while still exercising a real repo-level identity.
- Source, `cli/src/config.rs` lines 799–816 (tag `v0.45.1`), which resolves the ambiguity of where
  the env layer sits:
  <https://github.com/jj-vcs/jj/blob/v0.45.1/cli/src/config.rs#L799-L816> —
  ```
  /// Sources from the lowest precedence:
  /// 1. Default
  /// 2. System config
  /// 3. Base environment variables
  /// 4. [User configs](https://docs.jj-vcs.dev/latest/config/)
  /// 5. Repo config
  /// 6. Workspace config
  /// 7. Override environment variables
  /// 8. Command-line arguments `--config` and `--config-file`
  ```
  `env_overrides_layer()` (same file, ~L874–910) is the layer that does
  `if let Ok(value) = env::var("JJ_USER") { layer.set_value("user.name", value) }` and the same for
  `JJ_EMAIL` → `user.email`. `--config`/`--config-file` are parsed into `ConfigSource::CommandArg`
  layers appended after that.

**Experiment A — the ladder, one commit per rung** (`$S/expA`):

```console
$ export JJ_CONFIG=$S/expA-user.toml
$ cat $JJ_CONFIG
[user]
name = "User Level"
email = "user@level.test"
$ git init -q --initial-branch=main . && jj git init --colocate
### 1. user-level config only
$ JJ_TIMESTAMP=2001-01-01T00:00:00+00:00 jj new -m one
User Level <user@level.test> ; committer User Level <user@level.test> ; author_date=2001-01-01T00:00:00+0000 ; committer_date=2001-01-01T00:00:00+0000

### 2. repo-level config added (repo > user)
$ jj --ignore-working-copy config set --repo user.name "Repo Level"
Warning: This setting will only impact future commits.
The author of the working copy will stay "User Level <user@level.test>".
To change the working copy author, use "jj metaedit --update-author".
$ jj --ignore-working-copy config set --repo user.email "repo@level.test"
$ JJ_TIMESTAMP=2001-01-02T00:00:00+00:00 jj new -m two
Repo Level <repo@level.test> ; committer Repo Level <repo@level.test> ; author_date=2001-01-02T00:00:00+0000 ; committer_date=2001-01-02T00:00:00+0000

### 3. JJ_USER/JJ_EMAIL env (EnvOverrides > repo)
$ JJ_USER="Env Level" JJ_EMAIL=env@level.test JJ_TIMESTAMP=2001-01-03T00:00:00+00:00 jj new -m three
Env Level <env@level.test> ; committer Env Level <env@level.test> ; author_date=2001-01-03T00:00:00+0000 ; committer_date=2001-01-03T00:00:00+0000

### 4. per-command --config (CommandArg > EnvOverrides)
$ JJ_USER="Env Level" JJ_EMAIL=env@level.test JJ_TIMESTAMP=2001-01-04T00:00:00+00:00 \
    jj --config 'user.name=Cmd Level' --config 'user.email=cmd@level.test' new -m four
Cmd Level <cmd@level.test> ; committer Cmd Level <cmd@level.test> ; author_date=2001-01-04T00:00:00+0000 ; committer_date=2001-01-04T00:00:00+0000

### 5. resolved config with sources (overridden included)
$ jj config list user --include-overridden -T 'name ++ " = " ++ value ++ "   source=" ++ source ++ " overridden=" ++ if(overridden, "yes", "no") ++ "\n"'
user.name = "User Level"   source=user overridden=yes
user.email = "user@level.test"   source=user overridden=yes
user.name = "Repo Level"   source=repo overridden=no
user.email = "repo@level.test"   source=repo overridden=no
```

The same `config list` run with the env vars and the CLI overrides set shows all four rungs in
order — the source labels are the literal strings the binary emits:

```console
$ JJ_USER="Env Level" JJ_EMAIL="env@level.test" jj --config 'user.name=Cmd Level' --config 'user.email=cmd@level.test' \
    config list user --include-overridden -T 'name ++ " = " ++ value ++ " source=" ++ source ++ "\n"'
user.name = "User Level" source=user
user.email = "user@level.test" source=user
user.name = "Repo Level" source=repo
user.email = "repo@level.test" source=repo
user.name = "Env Level" source=env
user.email = "env@level.test" source=env
user.name = "Cmd Level" source=cli
user.email = "cmd@level.test" source=cli
```

Notes that matter operationally:

1. **`--config` vs `--config-file` is positional, not type-priority.** `parse_config_args` groups
   consecutive same-kind arguments into one layer and appends layers in argument order
   (`cli/src/config.rs` ~L920–960). Verified (`$S/expE`):

   ```console
   --config then --config-file: user.name = "File Level"
   --config-file then --config: user.name = "Cmd Level"
   two --config:                 user.name = "Second"
   two --config-file:            user.name = "File Two"
   ```

2. **An empty `JJ_USER`/`JJ_EMAIL` still overrides.** `env::var` returns `Ok("")`, so the override
   layer writes the empty string. With repo identity configured (`Repo Level`), a command run as
   `JJ_USER= JJ_EMAIL= jj …` produced the empty identity:

   ```console
   $ JJ_USER= JJ_EMAIL= JJ_TIMESTAMP=2001-01-05T00:00:00+00:00 jj new -m five
   Warning: Name and email not configured. Until configured, your commits will be created with the empty identity, and can't be pushed to remotes.
    <> ; committer  <> ; author_date=2001-01-05T00:00:00+0000 ; committer_date=2001-01-05T00:00:00+0000
   ```

3. **No identity is not a hard error for local commits.** With no user name/email at all
   (`JJ_CONFIG=` empty, no repo config), `jj new` exits 0 and creates a commit with empty name and
   email, after printing:

   ```console
   $ JJ_CONFIG= jj new -m x
   Warning: Name and email not configured. Until configured, your commits will be created with the empty identity, and can't be pushed to remotes.
   Hint: To configure, run:
     jj config set --user user.name "Some One"
     jj config set --user user.email "someone@example.com"
   @   <> ; committer  <> ; author_date=2026-10-20T11:13:44-0300 ; committer_date=2026-10-20T11:13:44-0300
   ```

   The push is what refuses it (F1.3).

4. **jj does not read Git's `user.name`/`user.email`.** In a colocated repo with
   `git config user.name "Git Level"` / `user.email git@level.test` and no jj identity,
   the jj commit still has an empty signature (`$S/expB/gitonly`):

   ```console
   $ git config user.name "Git Level"; git config user.email "git@level.test"
   $ JJ_CONFIG= JJ_TIMESTAMP=2001-09-09T09:09:09+00:00 jj new -m g
   Warning: Name and email not configured. …
   rywxnmxnwtwm commit=38faed0fe0 author= <> adate=2001-09-09T09:09:09+0000 committer= <> cdate=2001-09-09T09:09:09+0000
   ```

   [INFERENCE] `git -C <lane> config user.*` is therefore cosmetic for jj-created commits; only
   jj's own config stack (or env/CLI) names the commit.

### F1.3 — What an empty identity does at push time

`jj git push` checks the pushed range and refuses empty signatures. Sandbox bare remote
(`$S/expE2`, `JJ_CONFIG=` empty, commit + bookmark `main`):

```console
$ JJ_CONFIG= jj git push --remote origin --bookmark main
Error: Won't push commit c06c1ae23c82 since it has no author and/or committer set
Hint: Rejected commit: qorrkszy c06c1ae2 main | (empty) emptyid
push exit=1
```

(Adjacent check observed in the same run: a commit with no description is rejected first with
`Error: Won't push commit 3e36b3744861 since it has no description`.)

### F1.4 — Where repo/workspace config lives (and what follows a copy)

`jj config path --repo` does **not** point inside the repo:

```console
$ jj config path --repo
/home/vgpnk/.config/jj/repos/9d69d2150c81857507a6/config.toml
$ cat .jj/repo/config-id
9d69d2150c81857507a6
```

The ID file is `.jj/repo/config-id`; the config directory is
`$XDG_CONFIG_HOME/jj/repos/<id>/config.toml` (`REPO_CONFIG_DIR = "repos"` in `cli/src/config.rs`
L60; `SecureConfig::new_repo` at `lib/src/secure_config.rs` L166 reads `config-id` at L371).
A copied repo carries the ID, so identity follows the copy — with an explicit warning
(`$S/expE2copy`):

```console
$ cp -a $S/expE2 $S/expE2copy && cd $S/expE2copy
$ jj config path --repo
Warning: Your repo appears to have been copied from /fast/scratch/jj-wave/JjDocIdentity/expE2/.jj/repo to /fast/scratch/jj-wave/JjDocIdentity/expE2copy/.jj/repo. The corresponding repo config file has also been copied.
/home/vgpnk/.config/jj/repos/1c7107dc5ca510574414/config.toml
$ JJ_TIMESTAMP=2005-02-01T00:00:00+00:00 jj new -m copied
$ jj --ignore-working-copy log -r @ -T 'author.name() ++ " <" ++ author.email() ++ ">\n"'
Signer A <signer@example.test>
```

Consequences: re-cloning a lane (new `.jj`) loses the repo identity until `jj-lane.sh init` runs
again; deleting a lane leaves the `~/.config/jj/repos/<id>/` directory behind (`jj config gc`
exists to find/remove config dirs whose repo path no longer exists — `jj help config` lists it).

---

## F2 — Author vs committer on creation and on rewrite

**Citations.**

- v0.45.1 glossary “Author date”: <https://docs.jj-vcs.dev/v0.45.1/glossary/#author-date> —
  > It is set when the commit is first authored and usually stays the same when the commit is rewritten.

  (19 words.)
- v0.45.1 glossary “Committer date”: <https://docs.jj-vcs.dev/v0.45.1/glossary/#committer-date> —
  > It is set for a new commit and updated whenever jj rewrites the commit

  (15 words; the page continues “such as when rebasing, describing, or squashing it”).
- `jj help metaedit` (0.45.1 binary):
  > Whenever any metadata is updated, the committer name, email, and timestamp are also updated for all rebased commits.

  (18 words.) And:
  > The name and email may come from the `JJ_USER` and `JJ_EMAIL` environment variables, as well as by passing `--config user.name` and `--config user.email`.

  (23 words.)
- Source, `lib/src/commit_builder.rs`:
  <https://github.com/jj-vcs/jj/blob/v0.45.1/lib/src/commit_builder.rs#L186-L260> —
  `for_new_commit` (L188) does `let signature = settings.signature();` (L195) and writes
  `author: signature.clone(), committer: signature` (L207–208). `for_rewrite_from` (L227) clones the
  predecessor and then `commit.committer = settings.signature();` (L235) — the author field is never
  touched except for the empty-field backfill at L238–243.
- Source, `lib/src/settings.rs` L206–213: `signature()` = `{ name: user_name, email: user_email,
  timestamp: debug.commit-timestamp or now }`.

**Experiment B — rebase with a different identity** (`$S/expB`, author `Author A`, rebase as
`Rebaser B`; timestamps pinned with `JJ_TIMESTAMP`, which sets `debug.commit-timestamp`):

```console
## before rebase (c1, c2) — built with JJ_TIMESTAMP 2001-01-02 / 2001-01-03
xukpnptknlkq commit=d12cffb176 author=Author A <a@example.test> adate=2001-01-02T00:00:00+0000 committer=Author A <a@example.test> cdate=2001-01-02T00:00:00+0000
onwrrnywmovu commit=0960b6e172 author=Author A <a@example.test> adate=2001-01-03T00:00:00+0000 committer=Author A <a@example.test> cdate=2001-01-03T00:00:00+0000

## rebase c1 and descendants onto dest as identity B
$ JJ_USER="Rebaser B" JJ_EMAIL=b@example.test JJ_TIMESTAMP=2010-05-05T05:05:05+00:00 \
    jj rebase -s <c1-change> -d <dest-change>
Rebased 2 commits to destination.

## after rebase (same change ids, new commit ids)
xukpnptknlkq commit=4277300bd5 author=Author A <a@example.test> adate=2001-01-02T00:00:00+0000 committer=Rebaser B <b@example.test> cdate=2010-05-05T05:05:05+0000
onwrrnywmovu commit=9fb5d51c45 author=Author A <a@example.test> adate=2001-01-03T00:00:00+0000 committer=Rebaser B <b@example.test> cdate=2010-05-05T05:05:05+0000

## the old commit object of c1 is still readable, identity unchanged, hidden
xukpnptknlkq commit=d12cffb176 author=Author A <a@example.test> adate=2001-01-02T00:00:00+0000 committer=Author A <a@example.test> cdate=2001-01-02T00:00:00+0000  hidden=yes

## git view of the rewritten c1
$ git cat-file -p 4277300bd5661e163bda9e813617e809ddc83e7a
tree 4b825dc642cb6eb9a060e54bf8d69288fbee4904
parent 3acbdf579e32b414a0d201f8f2307bfe4ccf1fc9
author Author A <a@example.test> 978393600 +0000
committer Rebaser B <b@example.test> 1273035905 +0000
change-id xukpnptknlkqoqomyrylpwwllkqmqmwo
```

`jj describe` behaves the same way (`$S/expB`):

```console
$ JJ_USER="Rebaser B" JJ_EMAIL=b@example.test JJ_TIMESTAMP=2010-06-06T06:06:06+00:00 \
    jj describe -r <c2-change> -m "c2 edited"
onwrrnywmovu commit=e9ad52ad04 author=Author A <a@example.test> adate=2001-01-03T00:00:00+0000 committer=Rebaser B <b@example.test> cdate=2010-06-06T06:06:06+0000
```

`jj metaedit --update-author` copies the committer (i.e. the current identity) into the author and
keeps the author timestamp; `--update-author-timestamp` also resets the author timestamp:

```console
## metaedit --update-author as identity B
$ JJ_USER="Rebaser B" JJ_EMAIL=b@example.test JJ_TIMESTAMP=2010-07-07T07:07:07+00:00 \
    jj metaedit -r <c1-change> --update-author
xukpnptknlkq commit=f30f8daf1c author=Rebaser B <b@example.test> adate=2001-01-02T00:00:00+0000 committer=Rebaser B <b@example.test> cdate=2010-07-07T07:07:07+0000

## metaedit --update-author --update-author-timestamp
xukpnptknlkq commit=a86dd432e2 author=Rebaser B <b@example.test> adate=2010-08-08T08:08:08+0000 committer=Rebaser B <b@example.test> cdate=2010-08-08T08:08:08+0000
```

Source for that behavior: `cli/src/commands/metaedit.rs` L196–206 —
`new_author.name = commit_builder.committer().name` / `.email` when `args.update_author`; the commit
builder's committer was just set from `settings.signature()` (current identity). Explicit
`--author "Name <email>"` bypasses the config stack for the author but still rewrites the committer
to the current identity (`$S/expE`):

```console
$ jj metaedit -r <change> --author "Explicit Person <explicit@example.test>"
Explicit Person <explicit@example.test> / Repo Level <repo@level.test>
```

### F2.1 — `jj commit` keeps `@`'s author and stamps the committer

`jj help commit`: with path arguments the selected changes stay in the current commit and the rest
move to a new working-copy commit; without paths it is “`jj describe` followed by `jj new`”.
Consequence: `@`'s **author is not changed by `jj commit`**, only the committer is re-stamped (and
the new `@` gets the current identity for both fields). Verified without any `--config`
(`$S/expD2`):

```console
## @ at init (created before repo config)
@:  author=Global User <global@example.test> committer=Global User <global@example.test>
## @ after jj new under JJ_USER=Third Seat
@:  author=Third Seat <third@example.test> committer=Third Seat <third@example.test>
## jj commit -m msg (no paths, NO metaedit)
@-: author=Third Seat <third@example.test> committer=lane-1-shokunin <lane-1@shokunin.local> desc=work committed
@:  author=lane-1-shokunin <lane-1@shokunin.local> committer=lane-1-shokunin <lane-1@shokunin.local>
## round 2: metaedit --update-author + commit under per-command --config
@-: author=lane-1-shokunin <lane-1@shokunin.local> committer=lane-1-shokunin <lane-1@shokunin.local> desc=work2
```

With a path argument the same identity outcome was observed (`$S/expD`): `jj commit -m work -- a.txt`
warned that the path matched no change (the file was untracked under `snapshot.auto-track="none()"`),
yet it still converted `@` into `@-` and created a new `@`. The committed `@-` kept
`author=Third Seat <third@example.test>` and received
`committer=lane-1-shokunin <lane-1@shokunin.local>`. A later tracked-file run (`$S/expL2`) committed
a real path-limited diff (`files=b.txt`) and likewise stamped the committer with the repo-config lane
identity (its author was already the lane identity after a working-copy reset, so it does not
re-demonstrate author preservation). That stamping is exactly the reason `jj-lane.sh` runs
`metaedit --update-author` before `jj commit -- <paths>`.

### F2.2 — Two code-level exceptions to “author untouched”

1. **Empty-author backfill.** If the old author name/email are empty strings, a rewrite fills them
   from the current identity (`commit_builder.rs` L238–243). Verified (`$S/expF`): a commit created
   with the empty identity, then rewritten after repo identity was configured, became
   `author=[Lane X|x@shokunin.local]`; a commit with a non-empty author (`Someone Else`) kept its
   author on the same kind of rewrite. So the first jj rewrite of a pre-identity commit *changes*
   its author rather than preserving an empty one.
2. **Discardable commits.** If author == committer and the commit is discardable (no description and
   empty), the rewrite resets the author timestamp to the committer timestamp (L245–255). This only
   affects empty placeholder commits.

### F2.3 — Old commit objects survive as hidden commits

The pre-rewrite commit is still readable by commit id (`hidden=yes` above) and in Git's object
database; the change id is stable, the commit id changes. Nothing in jj keeps the previous
committer for a rewritten commit — “committer” always means the process that produced *this* object.

---

## F3 — Signing on rewrite

**Citations.**

- Defaults (`jj config list --include-defaults`): `signing.backend = "none"`,
  `signing.behavior = "keep"`, `git.sign-on-push = false`.
- v0.45.1 config → “Commit Signing”:
  <https://docs.jj-vcs.dev/v0.45.1/config/#commit-signing> —
  > `keep`: if a change was signed before modification, and it was authored by you, attempt to sign it again after the modification.

  (20 words.)
  > `own`: sign all commits that were authored by you when you modify them.

  (13 words.) The same block defines `drop` (“drop that signing after modification”) and `force`
  (“sign all commits after modification, always”).
  > If not set then defaults to the key associated with `user.email`

  (11 words, about `signing.key` for gpg/gpgsm).
- Source, `lib/src/settings.rs` L104–117 — the exact predicate:
  ```rust
  pub fn should_sign(&self, commit: &Commit) -> bool {
      match self.behavior {
          SignBehavior::Drop => false,
          SignBehavior::Keep => {
              commit.secure_sig.is_some() && commit.author.email == self.user_email
          }
          SignBehavior::Own => commit.author.email == self.user_email,
          SignBehavior::Force => true,
      }
  }
  ```
  `user_email` is the *resolved* `user.email` (`lib/src/settings.rs` L141–142), so it follows the
  same precedence ladder as F1. The comparison is an exact string equality on the author email.
- Source, `cli/src/commands/git/push.rs` L805–825: `sign_commits_before_push` **forces**
  `sign_settings.behavior = SignBehavior::Own` and signs only `!commit.is_signed() &&
  sign_settings.should_sign(...)`, skipping immutable commits with a warning.

**Experiment C — behavior matrix** (`$S/expC2`, ssh signing with an explicit sandbox key; `sig=` is
`if(signature, "SIGNED", "unsigned")`; `gpgsig=` counts header lines in `git cat-file -p`; the
`force` rows come from the isolated `$S/expJ` run):

```console
### keep + unsigned commit authored by me, rewritten: stays unsigned
xpqutozw commit=7b2e3241b4 author=Signer A … sig=unsigned
xpqutozw commit=e611ae8be6 author=Signer A … sig=unsigned

### keep + signed commit authored by me, rewritten: re-signed
xpqutozw commit=83a6296bab author=Signer A … sig=SIGNED        (gpgsig=1)
xpqutozw commit=f5eba85d7b author=Signer A … sig=SIGNED        (gpgsig=1, commit 83a6296bab -> f5eba85d7b)

### keep + signed commit authored by OTHER, rewritten by me: signature dropped
rsmmzsmo commit=3f28af0daa author=Other C <c@example.test> cname=Signer A sig=SIGNED   (gpgsig=1)
rsmmzsmo commit=370231efa5 author=Other C <c@example.test> cname=Signer A sig=unsigned (gpgsig=0)

### own: the commit is already signed at creation (own signs on creation too), rewrite re-signs
nwlxlxzz commit=dee203a7ee author=Signer A … sig=SIGNED   (gpgsig=1)
nwlxlxzz commit=3e9f02d1a0 author=Signer A … sig=SIGNED   (gpgsig=1)
# NOTE: this row did not isolate unsigned→signed on rewrite, because `own` had already signed
# the commit when it was created. The `keep` row above (unsigned commit stays unsigned) and the
# `force` row below (unsigned foreign commit becomes signed) bracket the predicate, and the source
# at lib/src/settings.rs L104–117 confirms the exact condition.

### own + signed commit authored by OTHER, rewritten by me: signature dropped
xzlvkppl commit=55ca5b5960 author=Other D … sig=SIGNED     (gpgsig=1)
xzlvkppl commit=31fe38cb90 author=Other D … sig=unsigned   (gpgsig=0)

### force: both commits were created unsigned under behavior=drop (one mine, one foreign)
## $S/expJ — before
mine:    author=Signer A sig=unsigned commit=45746be426
foreign: author=Other F sig=unsigned commit=789949e70a
## after `jj config set --repo signing.behavior force` and rewriting both (current user Signer A)
mine:    author=Signer A sig=SIGNED commit=ae9664c89b
foreign: author=Other F sig=SIGNED commit=be9feecb9e
## git objects
qkymztrq… gpgsig=1
llkunkml… gpgsig=1

### drop, signed commit rewritten -> signature removed
rxzxutnl … sig=SIGNED (gpgsig=1 after jj sign)
rxzxutnl commit=47184a48 … sig=unsigned (gpgsig=0 after rewrite)
```

An additional probe (`$S/expE3`): a signed commit rewritten after `signing.backend` was set to
`none` loses its signature **silently** (`a52c1a9c72 sig=SIGNED` → `1f0367d975 sig=unsigned`,
`metaedit exit=0`). So “keep” is only a re-sign promise when a signing backend is configured;
with the default `backend = "none"` any rewrite of a signed commit drops the signature.

### F3.1 — Signing failures are hard errors (exit 255), not warnings

With `signing.backend=gpg`, `signing.behavior=own`, and the lane identity that has no key,
commit creation, `jj commit` and `jj rebase` all abort:

```console
$ JJ_USER="lane-1-shokunin" JJ_EMAIL="lane-1@shokunin.local" jj new -m gpgtest
Internal error: Unexpected error from backend
Caused by:
1: Could not write object of type commit
2: Signing error
3: GPG failed with exit status: 2:
gpg: skipped "lane-1@shokunin.local": No secret key
gpg: signing failed: No secret key
jj new exit=255
```

Same failure from the rewrite path (`$S/expG`, rebase a two-commit chain under gpg+own with lane
identity `y@shokunin.local`):

```console
$ jj rebase -s <c1> -d <dest>
rebase exit=255
Internal error: Unexpected error from backend
Caused by:
1: Could not write object of type commit
2: Signing error
3: GPG failed with exit status: 2:
gpg: skipped "y@shokunin.local": No secret key

## state after failed rebase — unchanged, no partial rewrite
2148aebe27 author=y@shokunin.local cname=Lane Y cdate=2007-01-01 sig=unsigned
```

An ssh backend with an unusable key fails the same way (`Internal error … Signing error … SSH sign
failed with exit status: 255: Couldn't load public key /tmp/jj-signing-key-…`). These sandboxes are
the cited failure states kept under `/fast/scratch/jj-wave/JjDocIdentity/expC2`, `expG`, `expE2`.

### F3.2 — `jj sign` itself is a rewrite

`jj sign -r <change>` changes the commit id and updates the committer timestamp while preserving
author name/date (`$S/expE`):

```console
before: Repo Level … adate=2004-03-01T00:00:00+0000 committer=Repo Level … cdate=2004-03-01T00:00:00+0000 sig=unsigned
after : Repo Level … adate=2004-03-01T00:00:00+0000 committer=Repo Level … cdate=2004-03-02T00:00:00+0000 sig=SIGNED
```

`jj help sign` states “revisions are always re-signed” and “While that leads to discomfort for
users, which sign with hardware devices, as of now we cannot reliably check if a commit is already
signed…”.

### F3.3 — `git.sign-on-push` rewrites commits at push time

`$S/expE3`, `signing.behavior=drop`, `git.sign-on-push=true`, ssh key configured, two unsigned
commits in the pushed range:

```console
$ jj git push --remote origin --bookmark main
Updated signatures of 2 commits.
Changes to push to origin:
  bookmark: main [add to c4fbc582304d]
push exit=0
remote main=c4fbc582304da79de61dadffbb975a9810edb4f7 local pre-push=60625aca538ad00ce9564c250d3688edb6ec5013
remote gpgsig lines: 1
author Signer A <signer@example.test> 1104537600 +0000
committer Signer A <signer@example.test> 1792505813 -0300     <- push time
```

Note the pushed hash differs from the pre-push hash and the committer date becomes the push time.
Control (`$S/expH`, no sign-on-push): local and remote hashes were identical
(`aed11e1300df…`), author/committer unchanged.

Source nuance vs docs: the docs say “All mutable unsigned commits being pushed will be signed prior
to pushing”, but 0.45.1 forces `SignBehavior::Own` before the check, so a foreign-authored commit in
the range is left unsigned (`$S/expI`, push range base+own2+foreign):

```console
Other Person <other@example.test> change-id ovpxuquzqz… gpgsig=0
Signer A <signer@example.test>   change-id xsnkzotlqnn… gpgsig=1
Signer A <signer@example.test>   change-id okrnlqutuo… gpgsig=1
```

---

## F4 — Consequence for the planned shokunin integration

The helper `/home/vgpnk/Projects/shokunin/scripts/hyaku/jj-lane.sh` was read, not executed. Its
identity-relevant lines are:

- `cmd_init`: `jj --ignore-working-copy config set --repo user.name "${id}-shokunin"` and
  `user.email "${id}@shokunin.local"` (plus `snapshot.auto-track`, `trunk()`, bookmark tracking).
- `cmd_commit`: `jj --config user.name=… --config user.email=… metaedit --update-author`, then
  `jj --config … commit -m "$msg" -- <paths>`, then `bookmark set`, then `do_push`.
- `do_push`: `jj git push`; on rejection `jj git fetch`, then
  `jj --ignore-immutable rebase -b "$tip" -d "${BRANCH}@origin"`, then `bookmark set`; three
  attempts. **No `--config` and no env scrubbing on the rebase or the push.**

Mapping the evidence onto that design:

1. **Init’s repo-level identity is the right mechanism, but it is not authoritative.** It is layer 5;
   `JJ_USER`/`JJ_EMAIL` (layer 7) and `--config` (layer 8) outrank it. The helper already forces
   layer 8 on the two commit-side commands, so the `--as <id>` protocol closure path is protected.
   Verified with `JJ_USER` set in the environment for the change and the helper-equivalent
   `metaedit`+`commit` under `--config` (`$S/expD`): both author and committer came out
   `lane-1-shokunin <lane-1@shokunin.local>`.

2. **The push-retry rebase is the hole.** `do_push` rewrites commits with no `--config`, so the
   committer is whatever the ladder resolves at that moment. With the lane repo config intact that
   is the lane identity (verified: rebase without `--config` → committer
   `lane-1-shokunin <lane-1@shokunin.local>`), but a closure that exports `JJ_USER`/`JJ_EMAIL`
   silently stamps a different committer while the author stays lane (`$S/expD`):

   ```console
   ## same rebase but the closure exported JJ_USER/JJ_EMAIL for a seat
   llwxxkmz commit=27ee9c988f author=lane-1-shokunin <lane-1@shokunin.local> committer=Seat Scratch <seat@example.test>
   ## protocol check
   lane-1-shokunin|lane-1@shokunin.local|Seat Scratch|seat@example.test
   ```

   That violates the invariant “every lane commit carries the lane identity” (as stated for author
   **and** committer in the helper header) for any commit the retry path rebases, and it is invisible
   to the helper, which only prints hashes. [INFERENCE] Closures that run with exported
   `JJ_USER`/`JJ_EMAIL` are plausible: the operator's own shell/config may export them for jj work.

3. **Empty env values are worse than unset values.** `JJ_USER=` / `JJ_EMAIL=` (exported empty, e.g.
   an unset template variable interpolated into an assignment) override the repo config with empty
   strings and produce commits that push refuses (`Won't push commit … has no author and/or
   committer set`). A wrapper must `unset JJ_USER JJ_EMAIL`, not assign empty values.

4. **Init does not verify identity.** If the repo config write is skipped or overwritten, commits
   are still created locally with an empty identity (exit 0) and the lane only fails later, at
   `do_push` (helper exit 3). A cheap `jj config list user.name/user.email --repo` assertion in
   `cmd_init` would turn that into an immediate, attributable failure at layer 5.

5. **Signing is inherited from the host and can block every lane write.** [INFERENCE from the
   documented layer order — not separately probed with a user-level-only signing config: a user
   `signing.backend` sits on layer 4 and the lane repo config (layer 5) does not set any
   `signing.*` key, so it stays in force.] Because the lane repo sets
   `user.email=<id>@shokunin.local`, `should_sign(Own)` treats lane
   commits as “mine” and tries to sign with the configured backend:
   - gpg/gpgsm without `signing.key` → key looked up by `user.email`; no key exists for
     `<id>@shokunin.local` → exit 255 on `metaedit`, `commit`, `rebase` (F3.1). The lane stops
     with an “Internal error” that looks like a jj bug, not a policy conflict.
   - `behavior = "keep"` is safe for unsigned lane commits (it only re-signs already-signed commits
     authored by the lane email), so the default behavior is not the hazard — `own`/`force` are.
   - `signing.backend = "none"` (default) means any signature a commit already had is dropped on
     rewrite, silently.
   - `git.sign-on-push = true` (host-level) makes `jj git push` rewrite lane commits to sign them,
     so the **“committed <hash>”** line the helper prints in `cmd_commit` is stale; the
     **“pushed <hash>”** line (read from `heads(${BRANCH}@origin)` after the push) remains correct.
     The lane rule “a cited hash must be the PUSHED hash” therefore stays satisfiable only if
     closures cite the pushed line, never the committed one. With gpg + lane identity, sign-on-push
     fails the push instead (helper exit 3).

6. **`jj commit -- <paths>` really does keep `@`’s author**, so the helper’s extra
   `metaedit --update-author` is required, not redundant. The per-command `--config` on that
   `metaedit` is also what makes it immune to `JJ_USER`/`JJ_EMAIL`: `--update-author` copies the
   builder’s committer, which is computed from the same CLI layer (`metaedit.rs` L196–206).

7. **Foreign-authored commits rebased by the helper keep their author.** `for_rewrite_from` only
   replaces the committer, so a cherry-picked or seat-authored commit moved by the push-retry
   rebase will end up `author=<someone>, committer=<lane>`. If the lane protocol literally requires
   author == lane identity for every commit in the pushed range, the helper would need
   `metaedit --update-author` on the rebased range (or the policy needs to say “committer identifies
   the lane”), because jj has no co-author field and will not rewrite the author on rebase.

8. **Git-side commits bypass all of this.** jj does not read Git’s `user.name` (F1.4) and does not
   rewrite commits made by `git commit`; a lane that falls back to Git writes commits with Git’s
   identity and Git’s signing behavior. [INFERENCE: Git’s commit identity behavior is standard Git,
   not probed here; the jj side is observed.] The invariant depends on jj (or on configuring both).

9. **Repo config is out-of-tree and keyed by `.jj/repo/config-id`.** Lane teardown should either
   leave the `~/.config/jj/repos/<id>/` directory (harmless, small) or reclaim it with
   `jj config gc`; copying a lane directory carries the identity with a warning; re-cloning loses it
   until `init` re-runs (which the helper does). Also note `jj config set --repo user.*` emits
   “This setting will only impact future commits…” twice during `init` because `@` already exists —
   stderr noise the helper currently passes through.

10. **A caller’s own `--config` can still outrank the helper’s.** Both the helper’s flags and a
    caller’s are layer 8; `parse_config_args` appends layers in argument order, so the **last**
    `--config` wins. A closure that appends `--config user.name=…` after the helper’s `--config`
    (or wraps the call in its own jj alias) would override the lane identity on the commit path.
    Closures do not do that today; the guard is that the helper’s flags stay last on the command
    line (or that the helper stops accepting pre-wrapped jj invocations).

---

## F5 — Recommendations

1. In `jj-lane.sh`, scrub the override-env layer at entry: `unset JJ_USER JJ_EMAIL` (unset, not
   empty assignment). This makes layer-5 repo identity authoritative for every command, including
   `do_push`’s `fetch`/`rebase`/`bookmark set`/`push`.
2. Additionally pass the lane identity to the push-retry rebase (and to `jj git push` if signing
   matters): `--config user.name=<id>-shokunin --config user.email=<id>@shokunin.local`. Belt and
   braces: this keeps the refutation to env overrides and makes the committer explicit in the
   command line, which is auditable.
3. Add an `init` self-check that fails loudly if `jj config list user.name --repo` or
   `user.email --repo` is empty, instead of discovering it at push time as exit 3.
4. Decide the signing policy per lane explicitly and pin it in the lane repo config:
   - unsigned lanes: `signing.backend = "none"` so the lane never signs (and a rewrite visibly
     discards any foreign signature instead of quietly relying on a backend lookup that may fail),
     or at minimum keep `behavior = "keep"` and never `own`/`force`;
   - signed lanes: `signing.backend = "ssh"` with an explicit `signing.key` belonging to the lane,
     and a test that the key is readable by the lane user;
   - if `git.sign-on-push` is enabled host-wide, either pin `git.sign-on-push = false` in the lane
     repo config or document that only the “pushed” hash is citable and that the “committed” hash
     may differ.
5. Document in the lane addendum: “author is preserved on rebase; committer is re-stamped with the
   resolved identity at rewrite time; a lane commit is identified by its committer.” Update the
   `jj-lane.sh` header comment if author equality is not intended for foreign-authored commits.
6. Keep closures off `git commit` inside lanes; if a Git fallback is unavoidable, configure Git’s
   `user.name`/`user.email` to the same lane identity and accept that jj will not treat it specially.
7. On lane teardown, optionally run `jj config gc` (or accept the stale
   `~/.config/jj/repos/<id>` dirs) so the out-of-tree repo config does not accumulate.

---

## F6 — Open uncertainties

- **Workspace-level config was not exercised.** The ordering “workspace above repo” comes from the
  source comment and docs (F1), not from an experiment. `jj config set --workspace` writes outside
  the workspace (`~/.config/jj/workspaces/<id>/`), and no live workspace config was touched.
- **GPG with a real per-lane key** was not tested; only the no-key failure and ssh-with-key success
  were. Whether a lane key is picked up when `signing.key` is left unset (it defaults to the key for
  `user.email`) was not tested with an actual secret key for `<id>@shokunin.local`.
- **`git.sign-on-push` inside the helper’s retry loop** (fetch → rebase → push, with sign-on-push
  rewriting between attempts) was not exercised end-to-end; only a single push was.
- **Sign-on-push + immutable commits**: source has a “Skipped signing N immutable commits” branch;
  not exercised. Lane commits should be mutable, but the helper’s `trunk() = <branch>@origin` alias
  could make some commits immutable in edge cases.
- **Whether jj reads `GIT_AUTHOR_*`/`GIT_COMMITTER_*`** was not tested. jj does not read Git config
  identity (tested), but the Git-style env variables were not probed.
- **`jj sign` on a commit whose author email differs from `user.email`** with `behavior=keep`: the
  explicit `jj sign` command signs regardless (it is manual), but the interaction with a subsequent
  rewrite was only tested for matching/other authors via `keep`.
- **Docs `latest` is v0.46.0**, not 0.45.1. All citations above use the v0.45.1 pages; the same
  sentences were checked against the binary’s `jj help -k config`, but other 0.46.0-only changes
  were not reviewed.
- **Concurrency**: whether two jj processes with different `--config` identities can interleave in
  one repo (operation log merge) was not tested; the helper’s `flock` serializes its own calls, but
  not other seats’ jj commands.
- **Repo config GC semantics** (`jj config gc`) were read from `jj help config`, not executed.

---

## Citation summary

| Claim | Source | Quote / excerpt |
|---|---|---|
| Layer order (user < repo < workspace < env < CLI) | <https://docs.jj-vcs.dev/v0.45.1/config/#config-files-and-toml> | “settings from earlier items in the list are overridden by the settings from later items if they disagree” |
| Env layer is above repo | <https://github.com/jj-vcs/jj/blob/v0.45.1/cli/src/config.rs#L799-L816> | “5. Repo config … 6. Workspace config … 7. Override environment variables … 8. Command-line arguments” |
| `--config` beats everything | <https://docs.jj-vcs.dev/v0.45.1/config/#specifying-config-on-the-command-line> | “This overrides settings defined in config files or environment variables.” |
| Author date preserved on rewrite | <https://docs.jj-vcs.dev/v0.45.1/glossary/#author-date> | “It is set when the commit is first authored and usually stays the same when the commit is rewritten.” |
| Committer date updated on rewrite | <https://docs.jj-vcs.dev/v0.45.1/glossary/#committer-date> | “It is set for a new commit and updated whenever jj rewrites the commit” |
| New commit gets one identity for both | <https://github.com/jj-vcs/jj/blob/v0.45.1/lib/src/commit_builder.rs#L195-L208> | `let signature = settings.signature();` … `author: signature.clone(), committer: signature` |
| Rewrite replaces committer only | <https://github.com/jj-vcs/jj/blob/v0.45.1/lib/src/commit_builder.rs#L227-L243> | `commit.committer = settings.signature();` … empty author fields backfilled |
| `--update-author` copies the committer | <https://github.com/jj-vcs/jj/blob/v0.45.1/cli/src/commands/metaedit.rs#L196-L206> | `new_author.name = commit_builder.committer().name.clone();` |
| Signing predicate | <https://github.com/jj-vcs/jj/blob/v0.45.1/lib/src/settings.rs#L104-L117> | `Keep => commit.secure_sig.is_some() && commit.author.email == self.user_email` |
| Signing behavior meanings | <https://docs.jj-vcs.dev/v0.45.1/config/#commit-signing> | “`keep`: if a change was signed before modification, and it was authored by you, attempt to sign it again…” |
| gpg key defaults to user.email | <https://docs.jj-vcs.dev/v0.45.1/config/#commit-signing> | “If not set then defaults to the key associated with `user.email`” |
| Sign-on-push forces own commits | <https://github.com/jj-vcs/jj/blob/v0.45.1/cli/src/commands/git/push.rs#L805-L825> | `sign_settings.behavior = SignBehavior::Own;` |
| `metaedit` documents env/CLI identity | `jj help metaedit` (0.45.1) | “The name and email may come from the `JJ_USER` and `JJ_EMAIL` environment variables, as well as by passing `--config user.name` and `--config user.email`.” |
