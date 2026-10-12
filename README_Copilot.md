# Copilot: it suggests, you verify and explain

GitHub Copilot is an AI programming assistant. It can suggest code in the editor,
explain selected code in chat, and help investigate an error. Its suggestions
may be wrong or may violate the task requirements. Generated code alone does
not demonstrate your understanding.

## Set up Copilot in Codespaces

1. Check your plan in [Copilot settings](https://github.com/settings/copilot).
   Copilot Student is for students verified through GitHub Education; activate
   the benefit after verification. If it is not available yet, use Copilot Free
   if your account is eligible.
2. Search for **GitHub Copilot**, publisher **GitHub**, in Extensions, or use the
   Copilot setup action in the status bar. Sign in with the same GitHub account.
   Check Chat as well; Copilot / Copilot Chat components may be managed separately
   depending on the editor version.
3. For these tasks, use a question-answering mode (**Ask**, if available). Do not
   delegate the entire assignment to Agent or allow automatic command execution.
4. Inline suggestions usually appear as faded “ghost text”. Read before accepting.
   `Tab` normally accepts a suggestion and `Esc` rejects it; shortcuts may vary.

Free plans have limits. Student does not mean unlimited access to every model;
the current documentation describes automatic model selection for Free and
Student. You do not need to buy Copilot Pro or select a particular model.

## Lab rules

- Complete Lab 1 and the initial Lab 2 debugging checkpoint without AI.
  Disable Copilot suggestions for Python from the Copilot menu if they appear.
- After the debugging checkpoint, enable Copilot and record your use in a journal.
- Do not send passwords, tokens, personal data, or someone else's private code in prompts.
- Do not accept commands you cannot explain. Inspect file changes with `git diff`.
- `.github/copilot-instructions.md` asks for hints and explanations. It is guidance,
  not a technical mechanism that prevents full solutions from being generated.

## Three tasks with evidence

**A. Explanation.** Select a fragment containing `print`, `sep`, and `end` from
`app.py`. Prompt: “Explain this fragment to a beginner. Predict the exact output,
including spaces and newlines. Do not modify the file.” Compare the response
with the output of a real run.

**B. A limited code suggestion.** Ask for a small calculation or formatting
fragment for `miniapp.py`. Prompt: “Suggest at most 5 lines of Python using only
variables, conversions, and print. The total must have two decimal places.
Explain every line. Do not execute commands or change other files.”
Accept or adapt only what you understand. Test all three cases in LAB_02.md.

**C. Critique.** Request a solution for the same calculator without initially
specifying input conversion or formatting. Inspect the suggestion for a
correctness risk or unnecessary complexity. If it is correct, explain a real
limitation, such as invalid input or an underspecified prompt, rather than
inventing an error. Rewrite the prompt with clear constraints and compare responses.

In `raspunsuri/copilot.md`, record the exact prompt, the relevant response, what
you accepted/rejected/adapted, your reason, the test, and the observed result.
Write explanations in your own words. Justify at least one rejection or adaptation.

## If you cannot access Copilot

Record the problem or error message and tell your instructor. Complete Python
and Git without AI. For the Copilot component, observe a demonstration by your
instructor or a classmate without sharing accounts, label it “observed”, and
independently test the fragment. Your instructor will arrange an individual
make-up activity. Do not claim individual Copilot use if you only observed a demonstration.
