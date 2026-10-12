# Codespaces and the Python extension

A Codespace is a cloud-hosted development environment. You see VS Code in your
browser, while the files, terminal, Git, and Python interpreter run in the cloud's
Linux environment. Do not confuse Codespaces with `github.dev`: the latter is a
web editor and does not provide the same terminal/interpreter execution environment.

## What this repository configures

`.devcontainer/devcontainer.json` uses the official devcontainers image for Python
3.12. No additional pip packages are required. Setup checks the Python and Git
versions. The configuration does not automatically install editor extensions:
installing or verifying the Python extension is an explicit learning task.

## Install or verify the Python extension in the Codespace

1. Open **Extensions** in the Codespaces editor's sidebar.
2. Search for **Python**, publisher **Microsoft**, identifier `ms-python.python`.
3. If it is missing, click **Install** for the Codespaces environment. If it is
   already installed, for example through Settings Sync, verify that it is enabled
   in the Codespace and record “already installed” in your journal. Do not reinstall it unnecessarily.
4. Open `app.py`. In the Command Palette (`F1` or `Ctrl+Shift+P`), select
   **Python: Select Interpreter** → the Python 3.12 interpreter in the container.
5. Run `python --version` in the terminal. Record that version and the interpreter selected in the editor.
6. Use **Run Python File in Terminal** for `app.py`. Compare its output with
   `python app.py` in the shell. The output should match.

The extension supports editing, running, and debugging; **it does not include
the Python interpreter**. The interpreter is already installed in this image.
Disabling the extension does not stop `python app.py` from working in the shell
as long as Python itself is installed.

## Identify the editor's main areas

Explorer shows files and folders. The editor shows the selected file's contents.
The terminal shows commands and output. Source Control shows changes and commits.
Explain in your journal where you wrote code and where you executed it.

## Stop and resume

After pushing and checking GitHub: `F1` → **Codespaces: Stop Current Codespace**,
or [github.com/codespaces](https://github.com/codespaces) → your Codespace's menu → Stop.
Closing the browser tab does not guarantee immediate shutdown. Reopen the same
Codespace for Lab 2; do not create another without a reason. Stopping preserves
the environment and files. Deleting it can lose files and commits you have not pushed.

## Included usage and costs

As checked on 12 October 2026, a personal Free account includes 120 core-hours and
15 GB of storage per month; Pro includes 180 core-hours and 20 GB. Core-hours are
not clock hours: 90 minutes on a 2-core machine uses about 3 core-hours; two labs
use about 6, plus any time the environment remains running. Storage usage continues
while a Codespace is stopped. Check current allowances in your account's billing settings.
Do not start a paid trial or enable paid usage for this assignment. If you have
no available allowance, tell your instructor and use the local alternative in DEPANARE.md.
