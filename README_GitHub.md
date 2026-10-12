# Git, GitHub, and submitting your code

**Git** tracks versions of your project. **GitHub** hosts the remote repository
and lets others read its code and history. **Codespaces** is your cloud development
environment, containing a working copy of the repository and local Git history.
In these labs, “local” means inside your Codespace, not on your laptop.

## Where is your change?

| State | Where is the change? | Can the instructor see it on GitHub? |
| --- | --- | --- |
| Typed, not saved | In the editor | No |
| Saved | In the Codespace's working copy | No |
| Added with `git add` | In staging: the selection for the next commit | No |
| Committed | In the Codespace's Git history | Not yet |
| Pushed | Also in the GitHub repository | Yes, if they have access |

`main` is the submission branch. `origin` is the usual name for your remote
repository. `origin/main` records the remote branch state known to Git.
A commit has a SHA identifier and a message. Use a message that describes the
change: `Complete print experiments` is more helpful than `update`.

## Working cycle in the terminal

1. Save your files: **File → Save All**, or `Ctrl+S` for the current file.
2. From the repository root, inspect your changes:

```bash
git status
git diff
```

3. Select the required files. For the first checkpoint:

```bash
git add app.py raspunsuri/lab1.md dovezi/terminal.txt
git diff --staged
git commit -m "Set up the environment and add a personal greeting"
git push origin main
```

Use the `git add` command for your current checkpoint. The final Lab 1 checkpoint
also includes `dovezi/output_lab1.txt`. `git diff --staged` shows what will enter
the commit. New files start as “untracked”. In `git status --short`, `??` means
untracked, ` M` means an unstaged modification, and `M ` means staged.
`git diff` shows unstaged changes to tracked files, not the contents of every new file.

4. Verify:

```bash
git status
git log --oneline -5
git rev-parse HEAD
git remote -v
```

A clean working tree **does not prove that you pushed**. You may still have local
commits that are missing from GitHub. Open your repository in the browser, compare
the latest commit SHA, then open `app.py` and read the change there.

## Using Source Control in the editor

Open Source Control in Codespaces, inspect the diff, click `+` beside the required
files to stage them, enter a message, then **Commit** and **Push / Sync Changes**.
Sync may both pull and push. In these labs, use the terminal for each operation
at least once so you can explain the process.

## Template, fork, and pull request

A template creates an independent repository with the starting files and a new
history. A fork keeps the connection to, and history of, its parent repository.
Use **Use this template**, not Fork, for this assignment.
Template changes do not automatically propagate to student copies.
A pull request proposes merging one branch into another. It is not required
for the basic submission; Lab 2 includes an optional exercise in your own copy.

## `.gitignore`

This file tells Git which new files to ignore, such as `.venv/`, `__pycache__/`,
`.env`, and `*.local.txt`. It does not automatically stop tracking files already
in Git. The files in `dovezi/` are submission evidence and are not ignored.
Do not commit passwords, tokens, identity documents, or classmates' personal data.
