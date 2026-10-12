# Lab 1 — my repository and first Python run

**90 minutes. Follow the steps together with your instructor.**

| Minutes | Activity |
| --- | --- |
| 0–10 | What GitHub, Codespaces, an editor, and a terminal do |
| 10–25 | Create your private copy and invite the instructor |
| 25–40 | Start Codespaces, install/verify the Python extension |
| 40–50 | Find files and try the terminal |
| 50–65 | First small change, commit, push, browser check |
| 65–80 | Write and run a few print statements |
| 80–90 | Repeat commit/push and submit |

## 1. Create your own working space

Follow the Start here section in README.md. Open your own repository, then
create a Codespace. In the editor, point to:

- **Explorer:** the list of files.
- **Editor:** where you change a file.
- **Terminal:** where you run commands and see output.
- **Source Control:** where you can see your changes.

Open `LAB_01.md`, `lab1.py`, and `LEARNING_LOG.md` from Explorer. Explain which
is Python code and which is a document. Check that the repository belongs to you.

## 2. Check the Python tools

1. Open Extensions in the sidebar. Search for **Python**, publisher **Microsoft**,
   identifier `ms-python.python`.
2. Click **Install** in the Codespace if it is missing. If already installed,
   verify it is enabled; record that in LEARNING_LOG.md.
3. Open `lab1.py`. Press `F1`, choose **Python: Select Interpreter**, and select
   the Python 3.12 interpreter from the Codespace.
4. Open **Terminal → New Terminal**. Run:

```bash
python --version
```

Python is already installed in the configured Codespace. The extension helps
the editor work with Python; the interpreter actually executes the code.
See CODESPACES_GUIDE.md if you need help finding either component.

## 3. Try the terminal

Run these commands one at a time:

```bash
pwd
ls
git remote -v
```

`pwd` shows your current folder. `ls` lists its files. `git remote -v` shows
the GitHub repository linked to your Codespace. It should contain your username.
Find `lab1.py` both in the terminal list and in Explorer.

In the terminal, run:

```bash
python lab1.py
```

You should see `Hello, world!`. The command starts Python and tells it which
file to run. Write Python code in the editor, not directly into the shell.

## 4. First commit and push

In `LEARNING_LOG.md`, enter your student code, username, repository URL, and
whether you installed or verified the Python extension. Add one sentence about
where you write code and where you run it. **Save All**.

Run these commands from the project folder:

```bash
git status
git add LEARNING_LOG.md
git commit -m "Record my repository and Codespaces setup"
git push
```

`git add` selects the file for the commit. Commit records the version; push
sends it to GitHub. Open your repository in a separate browser tab and read
LEARNING_LOG.md there. Show the instructor your first change on GitHub.
The instructor also checks that they can open your private repository.

## 5. Three small print exercises

Complete `lab1.py` yourself. Keep the first line and add two new print statements
so the program displays three lines:

```text
Hello, world!
I am YOUR ALIAS.
I can run Python in Codespaces.
```

Replace `YOUR ALIAS` with a first name or pseudonym. For these exercises, type
the code yourself; disable Copilot suggestions for Python if they appear.

Before running, say what you expect. Save, run `python lab1.py`, and compare.
Then run the same file using **Run Python File in Terminal** in the editor.
Both methods should display the same messages.

Change one message, save, and run again. Explain why the terminal's old output
does not change until you run the program again. Write one short observation
in the Lab 1 section of LEARNING_LOG.md.

## 6. Second commit, push, and submission

```bash
git status
git add lab1.py LEARNING_LOG.md
git commit -m "Write and run my first print statements"
git push
```

Open `lab1.py` on GitHub and confirm it contains your three print statements.
Follow SUBMISSION.md. You should have two commits of your own from this session.
Stop the Codespace when you finish; reopen it in Lab 2.

**Quick check:** show where you edit, where you run, and where the instructor
reads your pushed file. Explain what would happen if you saved but did not push.
