# Submission: code on GitHub, with instructor access

Submit individually. Before the lab, your instructor provides their GitHub
username, the repository naming code, the submission location, and both deadlines.
Ask if any of these are missing. Do not submit a private repository link in a public issue.

## At the end of each lab

1. Save and run your program. Run the checker for the current stage.
2. Use `git add`, commit, and **push** for all required files.
3. Check `main`, the remote URL, and your Git state using `git status` and `git remote -v`.
4. Run `git rev-parse HEAD` and copy the full SHA of the submitted commit.
5. Open your own repository in the browser on `main`, then open its latest commit.
   The browser SHA must match the terminal SHA. Read your code and journal there;
   do not submit the Codespace URL.
6. Check the instructor invitation. “Pending” does not mean access has been granted:
   your instructor must accept and confirm that they can open the private repository.
7. Submit the following in the specified LMS/form:

```text
Student code / group:
GitHub username:
Stage: L1 / L2
Repository: https://github.com/USERNAME/python-lab-2026-CODE
Commit: https://github.com/USERNAME/python-lab-2026-CODE/commit/FULL_SHA
Full SHA:
Local checks: PASS / problem encountered
Instructor access: confirmed / invitation pending
Copilot (L2): used individually / observed demonstration, make-up needed
```

Replace the example values; do not submit the empty template. If checks fail,
submit your progress and the exact error by the deadline; your instructor will
arrange follow-up. Do not claim confirmed access until your instructor has opened the repository.

## Required files

**L1:** `app.py`, `raspunsuri/lab1.md`, `dovezi/terminal.txt`, `dovezi/output_lab1.txt`.

**L2:** all L1 files, plus `miniapp.py`, the three programs in `exercitii/`,
`raspunsuri/lab2.md`, `raspunsuri/copilot.md`, and `dovezi/output_lab2.txt`.
Keep the guides and configuration. Screenshots or a ZIP alone are not enough;
your instructor must be able to read the source and history in the repository.

## After submission

The commit link submitted in the form identifies the version to be assessed.
You may keep working, but a new submission requires a new commit link according
to your instructor's rules. Do not try to include the final commit SHA inside
that same commit: the identifier is generated after creating the commit and
is submitted separately in the LMS/form.
