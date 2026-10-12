# Python: from source file to output

Python is a programming language. A `.py` file contains instructions written in
that language. The Python interpreter is the program that executes them.
In Codespaces, `python app.py` starts the interpreter and passes the filename as
an argument. Python can automate calculations, analyse data, and build applications.
Our first applications run in the terminal and do not have a graphical interface.

In a simple script, statements execute in order. Do not reduce this to “Python
always reads just one line at a time”: CPython compiles source into bytecode
before executing it. A syntax error in the file may prevent any output at all.

## What `print` does

`print` is a built-in function. By default, it writes text to standard output
(`stdout`), which the terminal displays. It does not save your source, create a
commit, automatically create a file, or open a web page.

```python
print("Hello!")
print(2 + 3)
print("2" + "3")
```

Output:

```text
Hello!
5
23
```

Quotation marks delimit a string (`str`) and are not printed. `2` is an integer
(`int`); `"2"` is text. `+` adds numbers but concatenates two strings.
A line starting with `#` is a comment and produces no output.
Calling `print()` without arguments produces a blank line by default.

| Fragment | Output | Explanation |
| --- | --- | --- |
| `print("A", "B")` | `A B` | The default separator is a space |
| `print("A", "B", sep="|")` | `A|B` | Explicit separator between arguments |
| `print("A", end=""); print("B")` | `AB` on one line | The first call does not end the line |
| `print("A\nB")` | `A` and `B` on separate lines | `\n` inside a string represents a newline |

Unless you set `end`, `print` adds `\n` at the end. Write the two calls on separate
source lines in your exercise; the semicolon only shortens the table example.
`sep` and `end` are named arguments and must be strings (or `None`).

## Variables and expressions

```python
alias = "Ada"
quantity = 2
unit_price = 12.5
total = quantity * unit_price
print(f"Total: {total:.2f}")
```

`=` assigns a value to a name. `*` multiplies values. `12.5` is a floating-point
number (`float`), written with a decimal point in Python. An f-string inserts
values into text: `{total:.2f}` displays exactly two decimal places.
The expression performs the calculation; `print` displays its result.

## `input`: reading a user's response

```python
alias = input("Alias: ")
print(f"Hello, {alias}!")
```

The program waits until you type a response in the terminal and press Enter.
`input` returns text. Convert numeric input before calculating:

```python
quantity = int(input("Quantity: "))
unit_price = float(input("Unit price: "))
```

`int("2")` produces 2; `float("12.5")` produces 12.5.
`int("two")` and `float("12,5")` raise `ValueError`. The required calculator
assumes valid input; validating invalid input is an optional extension.
In the REPL, entering `2 + 3` displays the result automatically. That expression
alone in a script does not display anything; use `print(2 + 3)` in a script.

## Three errors to investigate

| Error | Example | What to inspect |
| --- | --- | --- |
| `SyntaxError` | An unclosed parenthesis | Syntax; the file may not run at all |
| `NameError` | `print(message)` before defining `message` | Names, quotation marks, and assignment order |
| `TypeError` | `"Total: " + 5` | Incompatible types; use conversion, a comma, or an f-string |

Read the final line of an error, then the filename and line number.
Indentation matters for Python blocks. Our first statements are at the top
level, with no leading spaces. Names are case-sensitive: `print` and `Print`
are different names.

For each experiment: predict first, run it, compare, and explain the difference.
