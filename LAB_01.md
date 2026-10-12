# Lab 1 — write, run, explain, and submit (90 minutes)

Work without Copilot or other AI code generators. Your instructor can help with
setup and commands, but the predictions and explanations must be your own.
Keep `raspunsuri/lab1.md` open and complete it while you work.

| Minutes | Activity | Checkpoint |
| --- | --- | --- |
| 0–8 | GitHub / Codespace / editor / terminal | Identify the four components |
| 8–23 | Private copy, instructor access, Codespace, Python extension | Correct remote and working Python |
| 23–35 | Navigation and a file created in the terminal | `dovezi/terminal.txt` |
| 35–48 | First program, first commit and push | Your first commit visible in the browser |
| 48–70 | `print` experiments: predict → run → explain | Program and observation table |
| 70–80 | `.gitignore`, output file, local checks | Evidence and completed journal |
| 80–90 | Second commit, push, and submission | Matching SHA and instructor access |

## 1. Set up your environment

Follow README.md and README_Codespaces.md. Install/verify Microsoft Python and
select the interpreter. In the terminal, from the repository root:

```bash
pwd
ls
ls -a
python --version
git --version
git remote -v
git branch --show-current
```

Record the versions, branch (`main`), remote, and the purposes of four files or
folders. Do not copy every startup log. Show your instructor the enabled extension
and the selected interpreter.

## 2. Terminal and files

Follow the navigation exercise in README_Terminal.md and create
`dovezi/terminal.txt` with `printf`. In your journal, record the path before and
after `cd dovezi`, and explain why `python app.py` cannot find the file from that
folder. Return to the root with `cd ..` before the following commands.

## 3. First run and checkpoint 1

1. Read `app.py`. Predict the output, then run `python app.py`.
2. Add a variable named `alias` containing your first name or a pseudonym and a
   `print` call that produces `Hello, ALIAS!` using that variable. Avoid sensitive information.
3. Save and run the file both from the terminal and with **Run Python File in Terminal**.
4. Complete the Environment, Navigation, and First run sections of your journal.
5. Create your first commit:

```bash
git status
git diff
git add app.py raspunsuri/lab1.md dovezi/terminal.txt
git diff --staged
git commit -m "Set up the environment and add a personal greeting"
git push origin main
```

Open your own repository on GitHub and check the new greeting. Record the commit
SHA in your journal after creating the commit; that entry will be included in
your next commit. Your instructor checks that they can open your private repository.

## 4. `print` experiments

For each experiment, **record your prediction before running**, then run, record
the observed output, and explain it. Build `app.py` progressively, without input.
Keep the initial greeting and your personal greeting as the first two output lines.

| Experiment | Task | What to explain |
| --- | --- | --- |
| P1 | Display `GIT|PYTHON|TERMINAL` with one `print`, three arguments, and `sep` | Separator and absence of spaces |
| P2 | Use two `print` calls to display `Starting...done!` on one line | `end` on the first call |
| P3 | Add a `print()` call with no arguments | Why a blank line appears |
| P4 | Display the result of `2 + 3`, then of `"2" + "3"` | Numbers versus text |
| P5 | Display `Line 1` and `Line 2` using one `print` and `\n` | Newline inside a string |
| P6 | Display `Personal message: ` followed by your own message | Quotation marks and your chosen text |

Your final output must have **10 lines**, in this order (line 5 is blank):

```text
Hello, world!
Hello, ALIAS!
GIT|PYTHON|TERMINAL
Starting...done!

5
23
Line 1
Line 2
Personal message: YOUR MESSAGE
```

Replace `ALIAS` and `YOUR MESSAGE`. Use the required `sep`, `end`, `print()`, and
operations in the actual code. Writing one large string containing the expected
output does not meet the implementation requirements. Add at least two useful comments.

## 5. Ignored files and saved output

From the repository root:

```bash
printf 'Local experiment, not submitted.\n' > experiment.local.txt
git status --short
git check-ignore -v experiment.local.txt
python app.py > dovezi/output_lab1.txt
cat dovezi/output_lab1.txt
python tools/verifica.py lab1
```

Explain why `experiment.local.txt` does not appear as a new file to submit and
which `.gitignore` rule excludes it. Compare `cat app.py` and `python app.py`:
source text versus program output. Do not edit the checker to make your work pass.

## 6. Checkpoint 2 and submission

Complete your journal. Without AI, explain what your instructor could see after
only Save, after only commit, and after push.

```bash
git add app.py raspunsuri/lab1.md dovezi/output_lab1.txt
git diff --staged
git commit -m "Complete print experiments and Lab 1 evidence"
git push origin main
git status
git log --oneline -5
git rev-parse HEAD
```

Follow PREDARE.md. You need at least **2 commits of your own with meaningful
changes**, in addition to the template's initial commit. Do not create empty commits.
Stop the Codespace after verifying your submission in the browser.

## Individual check without notes (2 minutes)

Your instructor asks you to change the P1 separator from `|` to ` / `, predict
the output, run the program, and explain where you push your work. Restore the
required separator, save, and rerun. Include any permanent changes in a new commit.
