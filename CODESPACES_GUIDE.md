# Codespaces: your working environment

Codespaces gives you an online computer for programming. Your browser displays
the editor, while Python and the terminal run in the cloud. You do not need to
install Python on your laptop when using this environment.

## Start once, reopen later

In your own repository, choose **Code → Codespaces → Create codespace on main**.
Use a 2-core machine if offered. Wait for setup to finish. At the next session,
reopen the same environment from [github.com/codespaces](https://github.com/codespaces).

## Install or verify the Python extension

1. Open **Extensions** in the editor sidebar.
2. Search for **Python**, publisher **Microsoft**, identifier `ms-python.python`.
3. Install it in the Codespace if needed, or verify that it is already enabled.
4. Open a `.py` file. Press `F1` → **Python: Select Interpreter** → Python 3.12.
5. Open **Terminal → New Terminal** and run `python --version`.

The Python extension adds editor support. The Python interpreter runs your
program. They are separate. The interpreter is already included in this repository's setup.

## Know where you are working

Explorer lists files. The editor changes their contents. The terminal runs
commands such as `python lab1.py`. GitHub in the browser shows the version you
have pushed. Opening a web editor with the `.` key on GitHub is not the same
as opening a Codespace with a Python runtime and terminal.

## Finish safely

Save, commit, push, and verify GitHub before you finish. Then press `F1` and choose
**Codespaces: Stop Current Codespace**, or stop it from the Codespaces page.
Closing a tab does not guarantee immediate shutdown. Stopping keeps your work;
deleting a Codespace can lose files and commits that have not been pushed.
Use your included allowance; do not buy resources for this lab. If creation is
blocked, tell your instructor so they can help with an alternative setup.
