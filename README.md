# Your first Python lab

**GitHub • Codespaces • Copilot • print and variables**

One beginner session, with room for up to 120 minutes. Follow this page in order.
At the end, your instructor should be able to open your completed work on GitHub.

## What you will complete

| File | Your work |
| --- | --- |
| `print_practice.py` | Three manual prints, one Chat-generated print, one Copilot edits directly in the file, one inline print |
| `variables.py` | Three short exercises with text variables; optional text input |

This README contains the instructions.
Use `TROUBLESHOOTING.md` if something does not work.

### Short official reading

Read the indicated parts when you reach the matching step below. These are
reference pages; complete the exercises in this assignment repository.

| Before step | Official page | What to read |
| --- | --- | --- |
| 2 — Codespaces | [GitHub Codespaces quickstart](https://docs.github.com/en/codespaces/quickstart) | Introduction and Personalizing with an extension; look at the editor screenshots. Its example uses a different project; use this lab's repository and Python commands. |
| 4 — Python | [Python: text](https://docs.python.org/3.12/tutorial/introduction.html#text) and [print](https://docs.python.org/3.12/library/functions.html#print) | The opening text/quotation examples and the first paragraph about print. Skip the later operations and optional print arguments. |
| 5 — Upload | [VS Code: stage and commit](https://code.visualstudio.com/docs/sourcecontrol/quickstart#step-3-stage-and-commit) | The + button, message box, and Commit button. Use this lab's Push instructions for your existing repository. |
| 6 — Copilot | [Chat requests](https://code.visualstudio.com/docs/chat/chat-overview#send-a-chat-request), [reviewing AI edits](https://code.visualstudio.com/docs/chat/chat-overview#review-and-manage-changes), and [inline suggestions](https://code.visualstudio.com/docs/editing/ai-powered-suggestions#getting-your-first-suggestions) | Sending a prompt, reviewing file edits, and accepting a faint suggestion. |

For Python examples, `>>>` marks an interactive prompt: do not copy it into your
`.py` file. We run saved files in this lab. Links checked 14 October 2026.

## 1. Open your own assignment

Sign in to GitHub with your verified account. Follow the route your instructor
announced:

**Classroom 50 link:** open the assignment link, sign in, accept the course
organization invitation if prompted, and click **Accept assignment → Open
repository**. If it says **Not a member yet**, ask the instructor for help.

**GitHub template link:** open [the template](https://github.com/AlexandruIonIonascu/python-lab-2026),
click **Use this template → Create a new repository**, choose your own account
as Owner, name it `python-lab-2026-CODE` using your assigned student code, select
**Private**, and click **Create repository**. In your copy, click
**Settings → Collaborators → Add people** and invite `AlexandruIonIonascu`.
Your instructor must accept the invitation.

Check the owner and name at the top. Work in your assignment copy. A repository
is the project's files and recorded versions; GitHub holds the online copy.

## 2. Open Codespaces and the files

Read the Codespaces row in **Short official reading** above.

1. In your assignment repository, click **Code → Codespaces**.
2. Click an existing Codespace if listed. Otherwise click **Create codespace
   on main** and wait for the editor.
3. Keep the GitHub repository in another browser tab. You will use it to check
   that your work was uploaded.
4. In the editor, click **Explorer** on the left (the files icon). Open
   `README.md`. Click **Open Preview** at the top right to read it.

Codespaces provides a remote computer with a VS Code editor. Changes in this
editor do not appear on the GitHub website until you upload them.

In Explorer, `.py` files contain Python instructions and `.md` files contain
formatted text. Folders group files. Leave `.github/`, `.devcontainer/`, and
`.gitignore` unchanged: they prepare the environment.

## 3. Prepare Python and the terminal

Python is a programming language. Its interpreter runs the instructions in
`.py` files. The Python extension helps the editor work with those files.

1. Click **Extensions** on the left (the blocks icon).
2. Search **Python**, select **Microsoft — Python** (`ms-python.python`), and
   click **Install**. If installed already, check that it is enabled.
3. Open `print_practice.py`. Press **F1**, find **Python: Select Interpreter**,
   and select the supplied Python 3 interpreter.
4. Click the editor's top-left menu → **Terminal → New Terminal**. If that menu
   is hidden, press F1 and choose **Terminal: Create New Terminal**.
5. Type these commands in the terminal, pressing **Enter** after each:

   ```bash
   pwd
   ls
   python --version
   ```

The terminal accepts commands for the Codespace computer. `pwd` shows the current
folder; `ls` lists its files; the last command shows the Python version.
Find `print_practice.py` in both Explorer and the `ls` output.

## 4. Write three print statements yourself

Read the Python row in **Short official reading** above.

Open `print_practice.py`. Find **A. MY PRINTS**. Replace only the comment
`# Write your three print statements here.` with these three lines:

```python
print("Hello, Python!")
print("I am learning to use Codespaces.")
print("This is my first program.")
```

Leave sections B, C, and D empty for now. If an AI suggestion appears while you
are typing, press **Esc** to dismiss it. Write these lines yourself.

1. Click the editor menu **File → Save All**. The unsaved dots on file tabs
   should disappear. You can also save a single file with **Ctrl+S** or
   **Cmd+S** on macOS.
2. Predict the three lines you will see.
3. In the terminal, type `python print_practice.py` and press **Enter**.
4. Check that the output matches the three messages, in that order.

`print` displays a value. Here, Python runs in the terminal, so the messages
appear there. Quotes mark text; the quotes and `print(...)` do not appear in
the output. Lines starting with `#` are comments and are not executed.


## 5. Upload your first work using buttons

Read the Upload row in **Short official reading** above.

| Action | What it does |
| --- | --- |
| Save | Writes your edits into the Codespace's files |
| Run | Executes the saved Python file |
| Commit | Records a version of your selected files in the Codespace |
| Push | Uploads that version to GitHub |

Use this button sequence each time you upload work:

1. Click **File → Save All**.
2. Click **Source Control** on the left (the branching icon).
3. Under **Changes**, click a filename to review your edits. At this checkpoint,
   the changed file should be `print_practice.py`.
4. Hover over each of those filenames and click its **+** button
   (**Stage Changes**). This selects the file for your commit and moves it to
   **Staged Changes**. Do this after saving your final edits.
5. In the message box at the top of Source Control, type
   **Write my first Python prints**.
6. Click **Commit**. If its button offers several actions, choose **Commit**.
   Wait for it to finish. The files should disappear from Staged Changes.
7. Open your GitHub tab and refresh. Your new code is still not there: you have
   recorded it in Codespaces but have not pushed it yet.
8. Return to Source Control. Click the **…** menu at the top of that panel →
   **Push**. If it is in a **Pull, Push** submenu, open that submenu and choose
   **Push**. Wait for the upload to finish.
9. Refresh GitHub again. Click `print_practice.py` and check that your three
   statements appear. Your commit message should also appear in the history.

**Check:** show the instructor or your partner your code on GitHub. You will
use the same buttons once more at the end. If Commit or Push reports an error,
keep the Codespace open and ask for help.

## 6. Add prints with Copilot in the marked sections

Read the Copilot row in **Short official reading** above.

You will add **one line to B, one to C, and one to D**. Keep your three lines
in A. Copilot is an AI assistant; read its suggestions before using them.

### Open Chat and choose a model

Click the **Copilot/Chat icon** in the editor's top bar and open Chat. Sign in
with the same GitHub account if requested. If missing, open Extensions and
install or enable **GitHub Copilot**, published by Microsoft; install **GitHub
Copilot Chat** if requested by the editor.

For B, choose **Ask** mode if offered. Click the model name or **Auto** beside the Chat
input to inspect the model picker. A model is the system that generates the
answer. Free and Student plans currently offer Auto; use the alternatives
below when named models cannot be selected. No paid upgrade is required.

### B. Get one complete print from Chat

1. Choose an available model, or leave **Auto** selected.
2. Send this prompt:

   > Give me exactly one Python print statement that displays "Hello from Copilot Chat." Return only that line. Do not edit my files.

3. Read the answer. It should use only `print` and quoted text.
4. In `print_practice.py`, under **B. PRINT FROM CHAT**, replace
   `# Paste one reviewed print statement here.` with **only the Python line**.
   Do not paste the Markdown fences or the conversation.
5. In the comment `# Selected model:`, add the name you selected, or `Auto`.

### C. Ask Copilot to complete a print directly in the file

Here Copilot edits the Python file for you. You review the change instead of
copying a response from Chat.

1. Open `print_practice.py` and find **C. AI EDITS THIS PRINT**. Replace
   `# Prepare an empty print here for Copilot to complete.` with `print()`.
   Click **File → Save All**. Leave A, B, and D unchanged.
2. Click **New Chat**. In the mode picker beside the Chat input, choose **Edit**
   if offered, otherwise **Agent**, so Copilot can edit files. Select a different
   available model from B if possible; otherwise use Auto. Fill in C's
   `# Selected model:` comment and save.
3. Type `#` in the Chat input and select `print_practice.py` from the file
   suggestions to attach it. Then send this prompt:

   > Edit print_practice.py directly. In section C, complete the empty print() so it displays "Copilot edited this file." Change only that print statement. Keep all section headings and all other code unchanged. Do not run commands, commit, or push.

4. Wait for Copilot to finish. Click the changed `print_practice.py` shown in
   its response to inspect the edit. Confirm that only the empty print in C was
   completed and that A, B, and D are unchanged. If **Keep/Accept** controls are
   shown, accept that edit. If the change is wrong, use **Undo/Reject** if shown
   and ask Copilot in the same Chat to correct only section C.
5. Return to the file in Explorer. Check that C contains one completed Python
   line with the requested message, then click **File → Save All**. Do not paste
   the Chat answer: the completed line must already be in the file.

If Copilot only replies with code, check that Edit/Agent mode is selected and
send **Apply this change to section C in the attached file**. Ask your instructor
for help if file editing is unavailable.

B uses a Chat response that you copy; C lets Copilot edit the file; D uses an
inline completion. Two Auto chats do not prove different models: record only
what you actually selected in the model comments.

### D. Inline suggestion

1. Find **D. INLINE SUGGESTION** in the same file. Leave its instruction comment
   `# Print the sentence: Hello from an inline suggestion.` in place.
2. Replace `# Start typing your print statement here.` by beginning to type
   `print(`. Wait for a faint suggestion in the editor.
3. Read it. **Tab** accepts the suggestion; **Esc** rejects it. Keep exactly one
   complete print statement under D. If no suggestion appears, ask for help,
   then write the line manually and tell the instructor.

Inline suggestions appear inside the editor; Chat responses appear in the Chat
panel. Changing the Chat model does not change the inline completion model.
If available, the top-bar Chat menu → **Configure Inline Suggestions… → Change
Completions Model…** lets you inspect that separate setting. If absent, continue.

**Now save and run once:** click File → Save All, then run
`python print_practice.py`. You should see **six lines**: three from A, one from
B, one from C, and one from D. If necessary, fix the relevant section and rerun.

If Chat is unavailable, watch the instructor demo and write the missing lines
manually. Tell your instructor which feature was unavailable; they will arrange
hands-on follow-up when access is available.

## 7. Complete three small variable exercises

A variable is a name for a value. For example:

```python
name = "Alex"
print(name)
```

`=` stores the text under the name. `print(name)` displays its value. Names
must be defined before use, and spelling/capitalization must match.

Open `variables.py`. Replace each write-here comment with your code, keeping the
section headings. Complete all three sections **before running**:

| Section in the file | What to write | Expected output |
| --- | --- | --- |
| A. NAME AND COURSE | Store `Alex` in `student_name` and `Python` in `course_name`. Print each variable on its own line. | Alex, then Python |
| B. TEXT OR VARIABLE | Print the quoted text `"course_name"`, then print the variable `course_name`. | course_name, then Python |
| C. A NEW VALUE | Store `Ready` in `status_message` and print it. Store `Finished` in the same variable and print it again. | Ready, then Finished |

Write these yourself. You may ask Copilot to explain one line if needed.
Click **File → Save All**, then run `python variables.py` once. Check the six
output lines against the table.

**Optional:** under **D. OPTIONAL INPUT**, replace the write-here comment with
`colour = input("Favourite colour: ")` and `print(colour)` on separate lines.
Save and run. When the program waits, type a colour **in the terminal** and press
Enter. `input` gives you text, which is stored in `colour` and then printed.

## 8. Upload and submit your finished work

1. Click **File → Save All**. Your Python programs should have run successfully.
2. Repeat the buttons in step 5: **Source Control → review changes → + beside
   each changed assignment file → message → Commit → … → Push**.
   This time include `print_practice.py` and `variables.py`.
   Use the message **Complete my first Python lab**.
3. After Push finishes, check that **Changes** and **Staged Changes** are empty.
   Empty lists alone do not prove upload: also perform the next check.
4. Refresh GitHub. Open both Python files and check that the completed sections
   appear. Confirm the latest commit message is **Complete my first Python lab**.
5. Click that commit message to open the commit, then copy its browser URL.
   Submit your **student code, repository URL, and final commit URL** in the
   LMS/form specified by your instructor.

For a personal template copy, confirm your instructor accepted the collaborator
invitation. Classroom 50 manages instructor access through the organization;
this lab is intended to use submission on pushes to the default branch.

## 9. Stop the Codespace safely

Before leaving: **Save All → Commit → Push → check the completed files on GitHub**.
Stopping a Codespace does not submit your work. Closing its browser tab does not
stop it immediately.

1. Open [Your Codespaces](https://github.com/codespaces).
2. Find the name and repository of the Codespace you used.
3. Click its **… → Stop codespace**. Check that it is stopped, then close the
   editor tab. Choose Stop, not Delete.
4. If you have other running Codespaces, open each one that might contain work.
   Save, commit, push, and check its GitHub copy before stopping it. Each
   Codespace has its own files; uploading from one does not save another's edits.
   Ask for help if different versions or upload errors appear.

To continue later, return to Your Codespaces and click the **same Codespace**.
Stopping keeps saved files, but storage still counts and Codespaces can expire.
Your pushed work remains in the GitHub repository.
