# Lab 2 — practise the workflow and use Copilot

**90 minutes. Most of this session is about GitHub, Codespaces, and Copilot.**
The final programming tasks use only print statements and variables.

| Minutes | Activity |
| --- | --- |
| 0–15 | Reopen the same Codespace and find your Lab 1 work |
| 15–30 | Make a small change and repeat commit/push |
| 30–50 | Set up Copilot and ask it to explain a print statement |
| 50–60 | Read, accept or adapt, run, and explain one small suggestion |
| 60–80 | Short print and variable exercises |
| 80–90 | Commit, push, and submit |

## 1. Find your work again

Open [github.com/codespaces](https://github.com/codespaces) and reopen the same
Codespace from Lab 1. In Explorer, open `lab1.py` and `LEARNING_LOG.md`.

```bash
git status
git remote -v
python lab1.py
```

Check that your remote is your own repository. Open the same file on GitHub
and find the change you submitted in Lab 1. Tell a partner what each action
means: **Save, Run, Commit, Push**. The instructor may ask you to demonstrate.

## 2. Repeat a change from start to finish

Change the final message in `lab1.py` to:

```text
I am ready for Lab 2.
```

Save and rerun the program. Before pushing, look at the file on GitHub: it should
still have your old message. Now publish the change:

```bash
git status
git add lab1.py
git commit -m "Update my message for Lab 2"
git push
```

Refresh GitHub and find the new message. This is the first checkpoint of Lab 2.
In LEARNING_LOG.md, write one sentence explaining the before/after observation.

## 3. Set up Copilot and ask for an explanation

Follow COPILOT_GUIDE.md to check your account, enable Copilot in the editor, and
open Chat. Use the question-answering/Ask mode if available.

Select one print statement from `lab1.py` and ask:

```text
Explain this line to a beginner. What will appear in the terminal?
Do not change any files. Use a short explanation.
```

Run the file and check the explanation against the real output. In the Copilot
section of LEARNING_LOG.md, record your prompt and a one-sentence explanation
in your own words. Your instructor may ask you to explain it without looking at Chat.

## 4. Try one small suggestion

Ask Copilot:

```text
Suggest one Python print statement with a friendly message about learning.
Use only print and quoted text. Do not modify files or run commands.
```

Read the response. Decide whether to accept it, change the message, or reject it.
Add one suitable print statement at the end of `lab1.py`, save, and run.
If Copilot proposes something you do not understand, ask it to simplify it.
Record the suggested line, your decision, and the output in LEARNING_LOG.md.

You can also try a comment such as `# Print a friendly learning message` to see
an inline suggestion. Read it before pressing Tab. Showing a suggestion is not
enough: you must run the accepted code and explain what it does.

## 5. Final exercises: print and variables

Your instructor demonstrates the example in PYTHON_GUIDE.md first.
Open `lab2.py`. Keep the exercise comments and complete the tasks below, in order.
Type your first attempt yourself, with Copilot suggestions disabled. You can
ask Copilot for a short explanation afterwards, then verify it by running.

**A. Two lines of text.** Add two print statements that display:

```text
My second Python lab
I am practising variables.
```

**B. Store and print a name.** Create a variable named `student_name` containing
a first name or pseudonym. Print its value twice using the variable each time.
Changing the assignment should change both output lines.

**C. Change a value.** Create a variable named `message` containing `First message`.
Print it. Assign `Updated message` to that same variable and print it again.
Predict the two lines before you run.

**D. Print two variables.** Create `course_name` and `group_name`, each containing
text of your choice. Print their values on separate lines. Do not print the
variable names in quotation marks: print the values they refer to.

Run `python lab2.py`. Change one of your variable values, save, and run again.
Tell the instructor which output lines changed and why. Add a short answer
to the Variables section of LEARNING_LOG.md.

### Optional, only if time remains: text input

Create `input_practice.py` in Explorer. Read one name with
`student_name = input("What is your name? ")`, then print the variable.
Run `python input_practice.py`, type a fictional name in the terminal, and press
Enter. Run again with a different name. Explain where the user's text is stored.
This is optional and is not needed for the required submission.

## 6. Final commit and submission

Save all files, then:

```bash
git status
git add lab1.py lab2.py LEARNING_LOG.md
git commit -m "Practise Copilot, print statements, and variables"
git push
```

If you completed the optional task, add `input_practice.py` before committing.
Open your repository in the browser and read `lab2.py` and LEARNING_LOG.md.
Follow SUBMISSION.md and stop your Codespace.

**Quick check:** without Copilot, change a variable, predict the output, run,
and show the instructor where your final version is on GitHub.
