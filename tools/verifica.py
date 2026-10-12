"""Formative checks. Does not assess understanding or confirm a GitHub push."""
import argparse
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

def check(ok, message):
    print(("PASS: " if ok else "FAIL: ") + message)
    if not ok:
        errors.append(message)

def run(relative, data=""):
    path = ROOT / relative
    if not path.is_file():
        check(False, f"Missing {relative}")
        return None
    try:
        result = subprocess.run(
            [sys.executable, str(path)], input=data, capture_output=True,
            text=True, encoding="utf-8", cwd=ROOT, timeout=5,
        )
    except subprocess.TimeoutExpired:
        check(False, f"{relative}: exceeded the 5-second timeout")
        return None
    check(result.returncode == 0, f"{relative}: runs without an error")
    if result.returncode != 0:
        print(result.stderr[-1500:])
        return None
    return result.stdout

def evidence(relative, actual=None):
    path = ROOT / relative
    check(path.is_file() and bool(path.read_text(encoding="utf-8").strip()),
          f"{relative}: exists and contains text")
    if actual is not None and path.is_file():
        check(path.read_text(encoding="utf-8") == actual,
              f"{relative}: matches the current program output")

def journal(relative):
    path = ROOT / relative
    if not path.is_file():
        check(False, f"Missing {relative}")
        return
    text = path.read_text(encoding="utf-8")
    check("[complete]" not in text and "[choose]" not in text,
          f"{relative}: no unfilled placeholder markers")
    print("INFO: journal explanations and evidence require manual assessment.")

def lab1():
    output = run("app.py")
    if output is not None:
        lines = output.splitlines()
        check(len(lines) == 10, "app.py: exactly 10 output lines")
        if len(lines) == 10:
            fixed = {0:"Hello, world!", 2:"GIT|PYTHON|TERMINAL",
                     3:"Starting...done!", 4:"", 5:"5", 6:"23",
                     7:"Line 1", 8:"Line 2"}
            for i, expected in fixed.items():
                check(lines[i] == expected, f"app.py: line {i+1} = {expected!r}")
            check(lines[1].startswith("Hello, ") and lines[1].endswith("!")
                  and len(lines[1]) > len("Hello, !"), "app.py: greeting contains an alias")
            check(lines[9].startswith("Personal message: ")
                  and bool(lines[9][len("Personal message: "):].strip()),
                  "app.py: personal message")
        evidence("dovezi/output_lab1.txt", output)
    evidence("dovezi/terminal.txt")
    journal("raspunsuri/lab1.md")

def lab2():
    for name, expected in [
        ("eroare_sintaxa.py", "Starting debugging\n"),
        ("eroare_nume.py", "Learning Python\n"),
        ("eroare_tip.py", "Total: 5\n"),
    ]:
        output = run("exercitii/" + name)
        if output is not None:
            check(output == expected, f"{name}: correct output")
    first_output = None
    for alias, quantity, price, total in [
        ("Ada", "2", "12.5", "25.00"),
        ("Lin", "0", "9.99", "0.00"),
        ("Sam", "3", "0.1", "0.30"),
    ]:
        output = run("miniapp.py", f"{alias}\n{quantity}\n{price}\n")
        if first_output is None and alias == "Ada":
            first_output = output
        if output is not None:
            lines = output.splitlines()
            check([line for line in lines if line.startswith("Hello, ")]
                  == [f"Hello, {alias}!"], f"miniapp.py: greeting for {alias}")
            check([line for line in lines if line.startswith("Total: ")]
                  == [f"Total: {total}"], f"miniapp.py: total for {quantity} × {price}")
    evidence("dovezi/output_lab2.txt", first_output)
    journal("raspunsuri/lab2.md")
    journal("raspunsuri/copilot.md")

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=["lab1", "lab2", "all"])
    args = parser.parse_args()
    if args.stage in ("lab1", "all"):
        lab1()
    if args.stage in ("lab2", "all"):
        lab2()
    print(f"\nResult: {'FAIL' if errors else 'PASS'} ({len(errors)} issues)")
    print("Grades and understanding require manual assessment and a demonstration.")
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
