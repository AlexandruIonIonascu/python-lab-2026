# Troubleshooting

| Symptom | Check and remedy |
| --- | --- |
| Use this template is missing | The instructor must enable Settings → Template repository; also check your access to the template |
| The remote points to the instructor's repository | Stop working there; create your own copy with Use this template and open Codespaces from it |
| `python: command not found` | Check that you are in Codespaces and setup has finished; try `python3 --version`; locally you may need `python3` or `py` |
| Python: Select Interpreter is missing | Verify that Microsoft Python is installed and enabled in the Codespace; reload the editor |
| `can't open file ... app.py` | Run `pwd` and `ls`; return to the repository root or use the correct path |
| I see source code instead of messages | `cat app.py` reads the source; `python app.py` executes it |
| Output does not change | Save All, check the file and path, then rerun; previous output remains in the terminal |
| I see `>>>` and Git commands fail | You are in the Python REPL; enter `exit()` and run Git in the shell |
| The program seems stuck | It may be waiting for `input`; type a response and Enter, or interrupt with Ctrl+C |
| `ValueError` when entering a price | Enter `12.5`, not `12,5`; the required calculator assumes valid input |
| `nothing to commit` | Check Save, `git status`, and staged files; the change may already be committed |
| `Author identity unknown` | Set `git config user.name "Your name"` and `git config user.email "YOUR_GITHUB_EMAIL"`; you may use your GitHub noreply address from Settings → Emails |
| Push 403 / Permission denied | Check the remote and signed-in account; you need write access to your own copy. Never paste a token into a file or chat |
| Push rejected / non-fast-forward | Remote changes exist; save and commit local work, then run `git pull --rebase origin main`. Ask your instructor for help with conflicts. Do not force push |
| Rebase conflict | Inspect `git status` and conflict markers with your instructor; `git rebase --abort` returns to the state before the rebase |
| Clean working tree but the instructor sees no changes | Check push, branch, remote, matching browser SHA, and instructor access |
| Instructor sees 404 for a private repository | Verify the invitation username and acceptance; send the repository URL, not the Codespace URL |
| Copilot does not suggest code | Check sign-in, extensions, Python suggestions, plan, and limits; use the procedure in README_Copilot.md |
| Codespaces cannot start / allowance exhausted | Read the exact error and check billing; do not purchase resources. Tell your instructor and use the local alternative |

## Local alternative if Codespaces is unavailable

Your instructor can help you install Git, Python 3.12 or newer, VS Code, and the
Microsoft Python extension. Clone **your own repository created from the template**
using Source Control → Clone Repository in VS Code, and authenticate with your
GitHub account. Open the cloned folder, select the interpreter, and run commands
from its terminal.

On macOS/Linux you may need `python3`; on Windows you may need `py`. For the shell
commands in these guides use Bash (Git Bash on Windows), or an equivalent command
demonstrated by your instructor to create `dovezi/terminal.txt`. Record your
environment and differences in the journal. Save / add / commit / push and the
browser verification are still required. `github.dev` alone does not replace a local runtime.
