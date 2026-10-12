# Your first Python lab: GitHub, Codespaces, and Copilot

**One beginner lab • allow up to 120 minutes • individual work • English**

Follow this README from start to finish. It contains all required instructions;
there is no separate Lab 1 or Lab 2. You will practise the tools first, then
finish with small exercises using `print` and text variables.

## Before you start

Have a GitHub account with a verified email and the assignment link from your
instructor. Use the same account throughout. Your instructor will announce the
submission location, student code, and deadline.

You need a browser; Python runs inside Codespaces. Copilot availability depends
on your account. You do not need to buy a plan for this lab. If a feature is
unavailable, tell your instructor and record that honestly.

## 1. Get your assignment repository

Use **only the distribution method your instructor announced**.

**If you received a Classroom 50 assignment link:**

1. Open that link and sign in with GitHub. Read the authorization screen.
2. Accept your course organization's invitation if prompted. If you see
   **Not a member yet**, ask your instructor to add your GitHub username to the roster.
3. Click **Accept assignment**. Wait for setup, then click **Open repository**.
4. Use this generated repository for all work. Skip the template steps below;
   instructor access is managed through the course organization.

**If you received the GitHub template link:**

1. Open [the course template](https://github.com/AlexandruIonIonascu/python-lab-2026).
2. Click **Use this template → Create a new repository**.
3. Choose your own account as Owner. Name it `python-lab-2026-CODE`, replacing
   `CODE` with the student code your instructor gave you. Choose **Private**,
   then **Create repository**.
4. In your copy, click **Settings → Collaborators → Add people** and invite
   `AlexandruIonIonascu`. Your instructor must accept before they can read it.

Check the owner and repository name at the top of GitHub. This must be your
assignment repository, rather than the instructor's source template.

A **repository** is a project containing files and their recorded history.
GitHub hosts a copy online. Open `print_practice.py` on GitHub: it contains
starter comments, not your completed work yet.

## 2. Open Codespaces and find your files

1. In your assignment repository, click **Code → Codespaces**.
2. If an existing Codespace is listed, click its name. Otherwise click
   **Create codespace on main** and wait for the editor to open.
3. Keep the GitHub repository open in another browser tab for checking pushes.
4. In the editor, click **Explorer** on the left. Click `README.md` and use
   **Open Preview** at the top right to read it, or the Command Palette command
   **Markdown: Open Preview**. Keep this guide available while editing code.

A **Codespace** is a remote development computer. The browser shows its VS Code
editor. Its files can change without the GitHub website changing: you must
commit and push to send your work there. Each Codespace has its own working
files; making a second one does not copy uncommitted changes from the first.

| File or folder | What it is for |
| --- | --- |
| `README.md` | The complete lab sequence; read it in order |
| `print_practice.py` | Your manual, Chat, and inline print statements |
| `variables.py` | The final small Python exercises |
| `LEARNING_LOG.md` | Your short answers and actual Copilot observations; fill it when asked below |
| `SUBMISSION.md` | Optional quick reminder of the final checklist already included here |
| `GITHUB_GUIDE.md`, `CODESPACES_GUIDE.md`, `COPILOT_GUIDE.md`, `PYTHON_GUIDE.md` | Optional short reminders; no additional exercises |
| `TROUBLESHOOTING.md` | Read only the relevant row if something goes wrong |
| `.devcontainer/` | Prepares Python in the Codespace |
| `.github/` | Contains beginner guidance for Copilot |
| `.gitignore` | Keeps generated files out of Git |
| `SOURCES.md`, `LICENSE` | Documentation links and reuse terms; no required exercises |

`.md` means Markdown: readable text with headings and formatting. `.py` means
Python source code. A folder groups files. Do not edit the configuration folders.

**Do it:** open both Python files in Explorer. Find the same filenames in your
GitHub tab. Open `LEARNING_LOG.md` and fill in your student code and repository URL.

## 3. Install the Python extension and open a terminal

Python is a programming language. A Python **interpreter** executes the
instructions you write in a `.py` file. An editor helps you write those
instructions; the Python extension adds Python support to VS Code.

1. Click **Extensions** on the left (the blocks icon).
2. Search for **Python**. Choose the extension published by **Microsoft**
   (`ms-python.python`) and click **Install**. If installed already, verify that
   it is enabled in this Codespace. This does not install an extension on your laptop.
3. Open `print_practice.py`. Open the Command Palette with **F1**, type
   **Python: Select Interpreter**, and select the provided Python 3 interpreter.
4. Open the editor menu at the top left: **Terminal → New Terminal**.
   If browser shortcuts interfere, use the Command Palette command
   **Terminal: Create New Terminal**.

A **terminal** is a place to type commands for the remote computer. Type the
following commands there, **one at a time**, pressing **Enter** after each:

```bash
pwd
ls
python --version
git remote -v
```

`pwd` shows the current folder. `ls` lists its files. `python --version` confirms
that the interpreter works. `git remote -v` shows where pushes will go: the URL
must identify your assignment repository.

**Do it:** point to `print_practice.py` in both Explorer and the `ls` output.
Explain which tab is the editor and which tab shows GitHub's online copy.
Commands go in the terminal; Python program lines go in the `.py` file.

## 4. Write, save, and run your first prints

In `print_practice.py`, below the manual-work comment, type these lines yourself.
Use a fictional name or your first name:

```python
print("Hello, Python!")
print("My name is Alex.")
print("I can run a Python file in a terminal.")
```

`print` sends a value to the program's output. In this lab you run the program
in a terminal, so that is where you see the output. Quotation marks identify
text. Each of these calls prints one line. The quotes and `print(...)` are
instructions; they do not appear in the displayed text.

1. Click the editor menu **File → Save**, or press **Ctrl+S**
   (**Cmd+S** on macOS). **File → Save All** saves every edited file.
   The unsaved dot on a file's tab should disappear. Autosave is off in this lab.
2. Before running, predict the three output lines.
3. In the terminal, run:

   ```bash
   python print_practice.py
   ```

4. Compare the output with your prediction. Change the second message, save,
   and run again. Earlier terminal output does not update automatically.
5. Swap the first and third Python lines, save, and run. Notice execution order.
6. Add `# This is my first program` on its own line. A line starting with `#`
   is a comment for a reader; Python does not print it.

If Python reports an error, read the filename and line number. Check matching
quotes and parentheses, save, and rerun. Ask for a hint if needed.

**Do it:** in `LEARNING_LOG.md`, answer the print/output question in your own words.

## 5. Make your first commit and push

These are four different actions:

| Action | What happens |
| --- | --- |
| Save | Your editor writes changes into the Codespace's files |
| Run | Python executes the saved program and shows output |
| Commit | Git records a snapshot of selected changes in this Codespace |
| Push | Git sends your commits to the repository on GitHub |

**Save alone is not submission. Commit alone is not submission.**

1. Click **File → Save All**.
2. In the terminal, run `git status`. Read which files changed.
3. Click **Source Control** on the left (the branching icon), then click a
   changed filename to inspect the difference. Return to the terminal.
4. Type these commands one at a time:

   ```bash
   git add print_practice.py LEARNING_LOG.md
   git commit -m "Write and run my first print statements"
   git push
   ```

   `git add` selects file changes for the next commit. `-m` supplies a short
   message explaining that commit. Wait for each command to finish.
5. Refresh your GitHub repository tab. Open `print_practice.py`. Check that your
   changed text appears. Find your commit message in the repository history.

**Do it:** change one printed message again and save. Refresh GitHub **before**
pushing: you should still see the previous text. Run the program, repeat the
commands above with the message `Update a print message`, and refresh again.
Now GitHub should show the new text. Explain the difference to your partner.

If a commit or push fails, keep the Codespace open and ask for help. A clean
working folder does not prove that a commit has been pushed.

## 6. Use Copilot Chat and inspect the model picker

Copilot is an AI assistant. An **LLM model** is the underlying system producing
its answers. You still decide which code to keep, run it, and explain it.

1. Click the Copilot/Chat icon in the editor's top bar, then **Open Chat** if a
   menu appears. Follow any sign-in instructions using your GitHub account.
2. If Chat is unavailable, open Extensions and install or enable Microsoft's
   **GitHub Copilot** extension. Install **GitHub Copilot Chat** if the editor
   requests it. Tell your instructor if your account has no access or hits a limit.
3. Use **Ask** mode if offered. Keep edits under your control: copy a small
   suggestion yourself into `print_practice.py`.
4. Find the model name or **Auto** near the Chat input. Click it to inspect
   the model picker. Model choices depend on your plan and organization policies.

### Chat comparison: the same prompt twice

Use this prompt:

> Suggest exactly one Python print statement that displays "I checked this suggestion." Explain it in one short sentence. Do not edit files. Do not use variables or other Python features.

**If you can select named models:** choose one available model, send the prompt,
then start a **New Chat** with the plus button, choose a different available
model in the picker, and send the identical prompt. If a model asks you to
approve paid usage, ask the instructor for the alternative exercise instead.

**If your picker only offers Auto:** Copilot Free and Copilot Student currently
use automatic model selection. Send the prompt in two new Auto chats and watch
the instructor demonstrate manual switching on an account that supports it.
Do not claim that two Auto requests necessarily used different models. If the
response reveals its actual model when you hover over it, you may record it;
otherwise write `not shown`. You do not need an upgrade or an API key.

For each response, read the suggestion, predict its output, and add one chosen
print line under the matching Chat comment in `print_practice.py`. Add a comment
with the model label you actually selected, for example `# Chat A: Auto`.
Save and run the file. Two models may give identical correct code; that is fine.
If a response uses extra concepts, reject it and repeat the restricted prompt.

In `LEARNING_LOG.md`, fill in both Chat rows and one short comparison. The
**mode** (such as Ask) and the **model** are separate choices.

## 7. Try one inline suggestion

An inline suggestion appears as faint text inside the code editor, rather than
as a Chat message. Changing the Chat model does **not** change the inline model.

1. In `print_practice.py`, find the inline section and type:

   ```python
   # Print the sentence: I reviewed an inline suggestion.
   ```

2. Press **Enter** and begin typing `print(`. Wait for a faint completion.
   If none appears, check the Copilot status menu and enable completions for Python.
3. Read it before accepting. **Tab** accepts; **Esc** dismisses it.
   Keep only a simple statement you understand. If necessary, finish it manually.
4. Save and run the file. Explain which text came from you and which from Copilot.
5. If your editor offers it, open the top-bar Chat menu →
   **Configure Inline Suggestions… → Change Completions Model…**.
   Inspect the choices and try another completion model if available. This is
   separate from the Chat picker. If absent, record `not available` and continue.

Record your decision and the inline model if shown in `LEARNING_LOG.md`.
If suggestions are unavailable, watch the instructor demo, write the print
manually, and label it accordingly; your instructor will arrange a short
hands-on follow-up if needed. Never label manual work as AI-generated.

Save all files, run the program, then repeat the commit/push routine:

```bash
git add print_practice.py LEARNING_LOG.md
git commit -m "Practise Copilot Chat and inline suggestions"
git push
```

Refresh GitHub and verify the new lines before moving on.

## 8. Finish with simple print and variable exercises

A **variable** is a name for a value. Assignment stores a value under that name:

```python
student_name = "Alex"
print(student_name)
print("student_name")
```

The second line prints `Alex`. The third prints the literal text `student_name`.
Quotes distinguish text from a variable name. Python names are case-sensitive:
`student_name` and `Student_name` are different names. Define a variable before
using it. `=` assigns a value; it is not an instruction to print anything.

Open `variables.py`. Complete A–D in order under the starter comments. Write
these yourself first; use Copilot for a small explanation if you get stuck.
After **each** exercise, save and run `python variables.py`.

**A — Two messages.** Write two print statements showing `My first Python lab`
and `I saved this file.` on separate lines. Predict the output before running.

**B — Name and course.** Store a fictional name in `student_name` and `Python`
in `course_name`. Print each variable on its own line. Change only the name's
value, save, and rerun. The printed name should change without changing its
print statement.

**C — Text versus a variable.** Print `"course_name"` and then `course_name`.
Explain why their outputs differ.

**D — A value changes.** Assign `"Ready"` to `status_message` and print it.
Then assign `"Submitted"` to the same variable and print it again. Before
running, predict both lines. Explain why they show different values.

**Optional — Input as text.** Ask for a favourite colour with
`colour = input("Favourite colour: ")`, then `print(colour)`. Save and run.
When the program waits, type a colour **in the terminal** and press **Enter**.
Run again with another colour. `input` returns the typed text and assignment
stores it in `colour`. No number conversion is needed.

Fill in the final variable answer in `LEARNING_LOG.md`. Use only short answers;
your instructor may ask you to change one value and explain the result live.

## 9. Submit and check the online version

1. Complete your learning log. Click **File → Save All**; check for unsaved dots.
2. Run `python print_practice.py` and `python variables.py`. Check their outputs.
3. Run `git status`, inspect the listed changes, and commit the intended files:

   ```bash
   git add print_practice.py variables.py LEARNING_LOG.md
   git commit -m "Complete print and variable exercises"
   git push
   git status
   git log -1 --oneline
   ```

4. Confirm `git push` succeeded. Afterward, `git status` should show a clean
   working tree and no commits ahead of the remote branch. If it says
   `nothing to commit`, you may already have committed: still run `git push`.
5. Refresh your GitHub repository. Open both Python files and the learning log.
   Confirm the latest commit message and code match the work in Codespaces.
6. Click the latest commit to copy its link. Submit your **student code,
   repository URL, and final commit URL** to the LMS/form your instructor specified.
   For Classroom 50, this lab should be configured for submission on pushes to
   the default branch; do not invent a tag or extra CLI submission step.
7. For a personal template copy, confirm your instructor accepted the collaborator
   invitation. For Classroom 50, instructor access is handled by the organization.

Your terminal output is not automatically stored on GitHub. Your submitted code,
learning log, and commit history are the evidence your instructor can read.

## 10. Stop safely, manage extra Codespaces, and resume

**Before ending work: Save All → run → commit → push → verify on GitHub.**
There is no automatic guarantee that closing a tab has submitted your assignment.

1. After the checks above, open [Your Codespaces](https://github.com/codespaces).
2. Match the repository and Codespace name to the one you used.
3. Click its **…** menu → **Stop codespace**. Confirm it is stopped before
   closing the editor tab. Closing the tab alone leaves it running until timeout.
4. If several Codespaces are running, inspect each one's repository and name.
   Open each one that might contain work, save and commit/push its intended
   changes, and verify its repository before stopping it through the same menu.
   Do not assume pushing from one has saved another's uncommitted files. If their
   work differs or a push is rejected, ask for help before combining it.
5. Choose **Stop**, rather than **Delete**. Stopping pauses computing and retains
   saved files, but storage still counts and stopped Codespaces can eventually
   expire. Pushed commits are your durable copy on GitHub.
6. Practise resuming: on Your Codespaces, click the same Codespace name and open
   it in the browser. Find your files and rerun a program. Then stop it again
   after checking there are no new edits or unpushed commits.

You have finished when you can demonstrate saving, running, committing, pushing,
checking GitHub, explaining a simple print/variable, reviewing a Copilot
suggestion, and stopping/resuming the correct Codespace.
