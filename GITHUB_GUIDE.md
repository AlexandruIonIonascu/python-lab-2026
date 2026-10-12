# GitHub: save, commit, and push

A repository is your project folder on GitHub, with a history of saved versions.
Git is the tool that records those versions. GitHub is where your instructor
reads your submitted work. Your Codespace contains a working copy of the project.

| Action | Meaning | Instructor sees the edit on GitHub? |
| --- | --- | --- |
| Save | Writes the file in your Codespace | No |
| Run | Executes the Python program | No |
| Commit | Records the selected changes in Git inside the Codespace | Not yet |
| Push | Sends your commits to GitHub | Yes, if access is accepted |

## The commands you need

Save your files first. Run these from the project folder, using the filenames
listed in the current lab:

```bash
git status
git add lab1.py LEARNING_LOG.md
git commit -m "Describe what I changed"
git push
```

`git status` shows changes. `git add` selects files for the next commit.
The commit message tells you what that version changed. `git push` publishes
your commits to your own repository.

## Check that the instructor can read it

Open your repository in the browser and read the changed file there. Find the
latest commit above the file list and open it. Copy that commit link for submission.
Your instructor must also accept the invitation to your private repository.
A clean `git status` alone does not prove that you pushed: check the browser.

Use the `main` branch already provided by your repository. You do not need to
create branches or pull requests for these labs. Create your student copy with
Use this template, then do all your work in that copy.
