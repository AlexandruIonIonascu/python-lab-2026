"""Verificare formativă. Nu evaluează înțelegerea și nu confirmă push-ul."""
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
        check(False, f"Lipsește {relative}")
        return None
    try:
        result = subprocess.run(
            [sys.executable, str(path)], input=data, capture_output=True,
            text=True, encoding="utf-8", cwd=ROOT, timeout=5,
        )
    except subprocess.TimeoutExpired:
        check(False, f"{relative}: depășește 5 secunde")
        return None
    check(result.returncode == 0, f"{relative}: rulează fără eroare")
    if result.returncode != 0:
        print(result.stderr[-1500:])
        return None
    return result.stdout

def evidence(relative, actual=None):
    path = ROOT / relative
    check(path.is_file() and bool(path.read_text(encoding="utf-8").strip()),
          f"{relative}: există și conține text")
    if actual is not None and path.is_file():
        check(path.read_text(encoding="utf-8") == actual,
              f"{relative}: corespunde rulării actuale")

def journal(relative):
    path = ROOT / relative
    if not path.is_file():
        check(False, f"Lipsește {relative}")
        return
    text = path.read_text(encoding="utf-8")
    check("[completează]" not in text and "[alege]" not in text,
          f"{relative}: fără marcajele necompletate")
    print("INFO: explicațiile și dovezile din jurnal se verifică manual.")

def lab1():
    output = run("app.py")
    if output is not None:
        lines = output.splitlines()
        check(len(lines) == 10, "app.py: exact 10 linii de output")
        if len(lines) == 10:
            fixed = {0:"Hello, world!", 2:"GIT|PYTHON|TERMINAL",
                     3:"Pornesc...gata!", 4:"", 5:"5", 6:"23",
                     7:"Linia 1", 8:"Linia 2"}
            for i, expected in fixed.items():
                check(lines[i] == expected, f"app.py: linia {i+1} = {expected!r}")
            check(lines[1].startswith("Salut, ") and lines[1].endswith("!")
                  and len(lines[1]) > len("Salut, !"), "app.py: salut cu alias")
            check(lines[9].startswith("Mesaj personal: ")
                  and bool(lines[9][len("Mesaj personal: "):].strip()),
                  "app.py: mesaj personal")
        evidence("dovezi/output_lab1.txt", output)
    evidence("dovezi/terminal.txt")
    journal("raspunsuri/lab1.md")

def lab2():
    for name, expected in [
        ("eroare_sintaxa.py", "Incep depanarea\n"),
        ("eroare_nume.py", "Invat Python\n"),
        ("eroare_tip.py", "Total: 5\n"),
    ]:
        output = run("exercitii/" + name)
        if output is not None:
            check(output == expected, f"{name}: output corect")
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
            check([line for line in lines if line.startswith("Salut, ")]
                  == [f"Salut, {alias}!"], f"miniapp.py: salut pentru {alias}")
            check([line for line in lines if line.startswith("Total: ")]
                  == [f"Total: {total}"], f"miniapp.py: total pentru {quantity} × {price}")
    evidence("dovezi/output_lab2.txt", first_output)
    journal("raspunsuri/lab2.md")
    journal("raspunsuri/copilot.md")

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("etapa", choices=["lab1", "lab2", "toate"])
    args = parser.parse_args()
    if args.etapa in ("lab1", "toate"):
        lab1()
    if args.etapa in ("lab2", "toate"):
        lab2()
    print(f"\nRezultat: {'FAIL' if errors else 'PASS'} ({len(errors)} probleme)")
    print("Nota și înțelegerea se stabilesc prin evaluare manuală și demonstrație.")
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
