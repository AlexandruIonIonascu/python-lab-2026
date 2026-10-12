# Python: print and variables

Python is a programming language. A `.py` file contains instructions. The Python
interpreter runs them. The editor is where you write those instructions; the
terminal is where you run the program and see its output.

## Run a file

Save the file in the editor, then enter this command in the terminal:

```bash
python lab1.py
```

This command starts Python and runs `lab1.py`. Do not type a Bash prompt symbol
such as `$` before it. Only the command belongs in the terminal.

## Print text

In a Python file:

```python
print("Hello!")
print("This is a second line.")
```

The terminal displays:

```text
Hello!
This is a second line.
```

`print` displays the supplied value. Quotation marks tell Python that the value
is text; the quotation marks themselves are not displayed. Each of these print
calls starts a new output line. A comment starting with `#` explains code and
does not produce output. Save and rerun whenever you change the program.
Printing does not save your code or publish it on GitHub.

## Store a value in a variable

```python
student_name = "Alex"
print(student_name)
```

The assignment gives the name `student_name` a text value. The print statement
uses that value and displays `Alex`. Compare:

```python
print(student_name)
print("student_name")
```

The first prints the variable's value. The second prints the literal text
`student_name`. Changing the assigned value changes later output that uses it.

```python
message = "Good morning"
print(message)
message = "Good afternoon"
print(message)
```

Predict the two lines, then run them. The second assignment changes the value
referred to by `message`. Use the exact same spelling when assigning and printing.

## Optional: read text from the user

```python
student_name = input("What is your name? ")
print(student_name)
```

The program waits for you to type in the terminal and press Enter. `input`
returns that text, which the assignment stores in `student_name`. The next line
prints it. We only use text input in this optional exercise.
