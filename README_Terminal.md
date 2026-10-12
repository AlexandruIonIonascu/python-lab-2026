# The terminal: commands in, results out

The terminal is a text interface. A **shell**, Bash in these labs, runs inside it,
reads your commands, and starts programs such as Python and Git.
The editor changes files; the terminal runs commands. A terminal is not a Python source file.

Open **Terminal → New Terminal** in Codespaces. The line waiting for a command
is called the prompt. Do not copy `$` or `>>>` prompt symbols from online examples.
The command blocks in these guides do not include those symbols.

| Command | What it does | What you should observe |
| --- | --- | --- |
| `pwd` | Shows the current directory | A path such as `/workspaces/python-lab-2026-CODE` |
| `ls` | Lists visible files and folders | `app.py`, guides, folders |
| `ls -a` | Also lists names starting with a dot | `.git`, `.gitignore`, `.devcontainer` |
| `cd dovezi` | Enters the evidence folder | The next `pwd` shows a different path |
| `cd ..` | Moves to the parent folder | You are back at the repository root |
| `mkdir -p dovezi` | Creates the folder if needed | It may produce no message |
| `cat app.py` | Displays the source as text | It does not execute Python |
| `python --version` | Requests the interpreter version | Python 3.12.x in the configured environment |
| `python app.py` | Runs the file using Python | Messages produced by the program |
| `git status` | Reports the Git state | File changes and branch/remote information |

## Shell commands or Python code?

In the shell, enter `python app.py`, `pwd`, or `git status`.
In `app.py`, write `print("Hello!")`. `print` is a Python function;
typing `print("Hello!")` directly into Bash may produce a syntax error.

Running `python` without a filename starts the interactive interpreter (REPL).
At the `>>>` prompt you can enter Python expressions, but `git status` is not
Python code. Enter `exit()` to return to the shell. `Ctrl+C` interrupts a running
program. If a program is waiting for `input`, type a response and press Enter,
or interrupt it with `Ctrl+C`.

## Redirecting output

From the repository root:

```bash
python app.py > dovezi/output_lab1.txt
cat dovezi/output_lab1.txt
```

The shell interprets `>` and writes standard output to a file, replacing that
file's previous contents if it exists. The program has run even though its
messages did not appear on screen. Errors may still appear in the terminal
because they use a separate error stream. The output file reaches GitHub only
after you add it, commit, and push.

## Navigation exercise

Run `pwd`, `ls`, `ls -a`, `cd dovezi`, `pwd`, `cd ..`, and `pwd`.
Record what changed in your journal. Create a file from the shell:

```bash
printf 'I created this file from the terminal.\n' > dovezi/terminal.txt
cat dovezi/terminal.txt
git status --short
```

Here, `printf` is a shell command, not Python's `print` function. Find the new
file in Explorer as well. Do not use recursive deletion commands in these labs.
