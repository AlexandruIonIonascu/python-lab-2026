# Lab 2 — debug, build, and evaluate Copilot (90 minutes)

Reopen the same Codespace and your existing repository. The first two sections
are completed without AI.

| Minutes | Activity | Checkpoint |
| --- | --- | --- |
| 0–10 | Individual recap and Lab 1 submission check | Explain Save / Run / Commit / Push |
| 10–27 | Three errors, before and after fixing | Debugging journal |
| 27–35 | Debugging commit and push | Your third commit visible on GitHub |
| 35–47 | `input`, conversions, and calculator requirements | Predict three results |
| 47–67 | Copilot explanation, limited suggestion, and critique | Decisions and tests in your journal |
| 67–80 | Implementation and three test cases | Correct output and evidence |
| 80–90 | Individual explanation, commit, push, and final submission | Your fourth commit and verified access |

## 1. Recap

From the root, run `git status`, `git remote -v`, `python app.py`, and
`python tools/verifica.py lab1`. Check your submitted Lab 1 commit in the browser.
Explain why closing a tab after Save is not enough. If you also worked in another
environment, synchronize using the guidance in DEPANARE.md.

## 2. Debug without Copilot

Run each program separately:

```bash
python exercitii/eroare_sintaxa.py
python exercitii/eroare_nume.py
python exercitii/eroare_tip.py
```

For each file, complete `raspunsuri/lab2.md`: your prediction, the final error
line, the indicated source line, the cause, your minimal change, and the output
after fixing. Fix the files so they display, respectively, exactly
`Starting debugging`, `Learning Python`, and `Total: 5`.
Do not delete the files or comment out the entire program. Rerun each file;
an editor warning disappearing is not proof that the fix works.

```bash
git add exercitii/eroare_sintaxa.py exercitii/eroare_nume.py exercitii/eroare_tip.py raspunsuri/lab2.md
git diff --staged
git commit -m "Fix three errors and explain the debugging process"
git push origin main
```

Record the SHA in your journal after the commit; it will enter your next commit.

## 3. Build a terminal cost calculator

In `miniapp.py`, build an application that:

1. Reads an alias with `input` and displays `Hello, ALIAS!`.
2. Reads a quantity (a nonnegative integer) and a unit price (a nonnegative number).
   Use a decimal point for prices: `12.5`, not `12,5`.
3. Converts the numeric inputs using `int` and `float`.
4. Calculates `total = quantity * unit_price` using the values read from the user.
5. Displays a line `Total: XX.XX` with exactly two decimal places and no currency
   symbol or other suffix.
6. Includes at least two useful comments and uses no external packages.

You may choose your input prompt text, but each prompt must end with `\n`, for
example `input("Alias:\n")`. This keeps the greeting and total on separate lines
even when input is supplied automatically. You can experiment with normal inline
prompts, but use the required form in your submitted application. Do not print
additional lines starting with `Hello, ` or `Total: `.

### Three required test cases

Record your predictions before running. Run `python miniapp.py` three times
and enter the following values, each on its own line:

| Case | Alias | Quantity | Unit price | Expected final line |
| --- | --- | --- | --- | --- |
| T1 | Ada | 2 | 12.5 | `Total: 25.00` |
| T2 | Lin | 0 | 9.99 | `Total: 0.00` |
| T3 | Sam | 3 | 0.1 | `Total: 0.30` |

Explain why T2 is an edge case and why T3 checks decimal formatting.
Do not hardcode the answers for these three cases. Your program must calculate
other valid quantities and prices as well. Your instructor will test a new case.

## 4. Copilot with evidence

Enable Copilot and complete tasks A, B, and C in README_Copilot.md.
Complete `raspunsuri/copilot.md` while you use it; do not invent prompts afterwards.
You may build the initial structure yourself and request only the limited help
specified in task B. Justify at least one adapted or rejected suggestion.
If access is unavailable, follow the demonstration and make-up procedure in the guide.

## 5. Checks and evidence

Save all files, then run:

```bash
python tools/verifica.py lab2
python tools/verifica.py all
```

The checker executes programs with a timeout and compares selected results.
It does not assess the quality of your explanations, actual Copilot use, or proof
of pushing. PASS is not your final grade. Implementation requirements are also
checked manually. The starter intentionally fails checks until you complete the tasks.

Create evidence that can be read in your repository:

```bash
printf 'Ada\n2\n12.5\n' | python miniapp.py > dovezi/output_lab2.txt
cat dovezi/output_lab2.txt
```

The shell pipe `|` sends `printf` output to the Python program's input.
Record the T2 and T3 outputs from your interactive runs in your journal as well.

## 6. Final submission

```bash
git add miniapp.py exercitii/eroare_sintaxa.py exercitii/eroare_nume.py exercitii/eroare_tip.py raspunsuri/lab2.md raspunsuri/copilot.md dovezi/output_lab2.txt
git diff --staged
git commit -m "Add the cost calculator and evaluate Copilot suggestions"
git push origin main
git status
git log --oneline -6
git rev-parse HEAD
```

Follow PREDARE.md. You should now have at least **4 meaningful commits of your own**:
two from Lab 1 and two more from Lab 2. The initial template commit does not count.
Stop the Codespace after checking the submission in the browser.

## Individual check without AI (2 minutes)

Your instructor chooses a new alias, quantity, and unit price. Predict the total,
run the application, and explain the type returned by `input` and why conversion
is needed. Show your final commit and a Copilot suggestion you adapted.

## Optional extensions after the required work

- Validate input with `try/except ValueError` and reject negative values. Explain
  the new blocks and test valid, invalid, and negative input. Preserve the required output for valid cases.
- Create a branch named `improve-messages`, add an explanatory comment, commit,
  run `git push -u origin improve-messages`, and open a pull request **in your own
  repository** targeting `main`. After merging, return to `main` and synchronize.
  The required submission must remain on `main`.
