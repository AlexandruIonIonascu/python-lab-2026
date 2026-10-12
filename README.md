# Your first Python applications: GitHub, terminal, Codespaces, and Copilot

**Two 90-minute labs • individual work • 2026 edition**

By the end, you will be able to write and run a Python application, explain its
terminal output, fix errors, evaluate Copilot suggestions, and submit your code
on GitHub using commit and push. No previous programming experience is required.
Read each section as you reach that step; you do not need to read every guide first.

## Before the first lab

1. Create a GitHub account and verify your email address. Remember your username.
2. Your instructor will provide the template link, their GitHub username, your
   student code, the submission location (LMS/form), and the two deadlines.
3. You may apply for [GitHub Education](https://github.com/settings/education/benefits)
   in advance. Approval is not required to start the lab.
4. Bring a browser and an internet connection. In Codespaces, Python runs in the
   cloud; you do not need to install it on your laptop. The Python editor extension
   is a separate component that you will install or verify during the lab.

## Create your own repository, then open Codespaces

1. Open the instructor's template → **Use this template → Create a new repository**.
   Do not choose “Open in a codespace” directly from the instructor's template.
2. Owner: your own account. Name: `python-lab-2026-CODE`, replacing `CODE` with the
   identifier provided by your instructor. Select **Private**. Leave “Include all
   branches” unchecked.
3. In your repository: **Settings → Collaborators** (the label may vary)
   → **Add people** → your instructor's exact username → send the invitation.
   Your instructor must accept it to read your private repository.
4. In **your own repository**: **Code → Codespaces → Create codespace on main**.
   Select 2 cores if a machine choice is offered. The first startup may take a few minutes.
5. Wait for setup to finish. Follow [the Codespaces guide](README_Codespaces.md)
   to install/verify the Python extension and select the interpreter.
6. In the Codespaces terminal, run `git remote -v`. The URL should contain your
   username and your repository name, not the instructor's repository.

**Work in your own copy. Do not submit a pull request to the instructor's template.**
Both labs use the same student repository and the same Codespace.

## What to do and submit

| Session | Instructions | Required work |
| --- | --- | --- |
| Lab 1 | [LAB_01.md](LAB_01.md) | `app.py`, your journal, a file created in the terminal, at least 2 commits of your own |
| Lab 2 | [LAB_02.md](LAB_02.md) | Calculator application, debugging exercises, Copilot journal, at least 2 further commits of your own |
| After each session | [Submission guide](PREDARE.md) | Repository URL + commit link + confirmed instructor access |

## Repository map

The existing paths are kept for compatibility. `exercitii/` contains exercises,
`raspunsuri/` contains your responses, and `dovezi/` contains evidence.

| File or folder | Purpose | Do you edit it? |
| --- | --- | --- |
| `README.md` | Starting point | Not required |
| `LAB_01.md`, `LAB_02.md` | Tasks and step-by-step instructions | No |
| `README_GitHub.md` | Git, repositories, commit, and push | No |
| `README_PY.md` | Python, `print`, `input`, and errors | No |
| `README_Terminal.md` | Commands and navigation | No |
| `README_Codespaces.md` | Cloud environment and extensions | No |
| `README_Copilot.md` | AI suggestions, explanations, and testing | No |
| `app.py` | Your first application | Yes, in Lab 1 |
| `miniapp.py` | Cost calculator | Yes, in Lab 2 |
| `exercitii/*.py` | Three programs with intentional errors | Yes, in Lab 2 |
| `raspunsuri/*.md` | Your evidence and explanations | Yes |
| `dovezi/` | Run output and a file created from the terminal | Yes |
| `tools/verifica.py` | Local checks for selected requirements | No |
| `.devcontainer/devcontainer.json` | Python 3.12 environment for Codespaces | No |
| `.github/workflows/verificare.yml` | Manually triggered GitHub Actions checks | No |
| `.github/copilot-instructions.md` | Educational guidance for Copilot | No |
| `.gitignore` | Rules for files that Git ignores | Only inspect it for the exercise |
| `LICENSE` | Material license | No |

Folders organize the project. `exercitii/example.py` is a relative path from the
repository root. Linux filenames are case-sensitive: `README_PY.md` and
`README_Python.md` are different names. Git tracks files, not empty folders.
The internal `.git/` folder stores local history; do not edit or delete it.

## Four different operations

**Save** writes a file in your Codespace. **Run** executes the program and produces
output. **Commit** records a version in the Codespace's local Git history.
**Push** sends those commits to GitHub, where your instructor can read them if
they have access. Running a program or committing without pushing is not a complete submission.

## Getting help

See [the troubleshooting guide](DEPANARE.md). If you cannot create a Codespace,
tell your instructor; a local setup alternative is included there. You do not
need a paid subscription for these labs. Official sources and their verification
date are listed in [SURSE.md](SURSE.md).
