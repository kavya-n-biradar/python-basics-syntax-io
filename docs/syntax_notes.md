# Python Syntax Notes: Indentation and Data Types

## Indentation

Python uses **indentation** (spaces at the start of a line) to show which lines belong together in a block. Many other languages use curly braces `{ }` for this, but in Python the indentation is part of the syntax.

```python
age = 18
if age >= 18:
    print("Adult")      # indented: runs only if the condition is true
    print("Can vote")   # same block
print("Done")           # not indented: always runs
```

Rules:
- Use **4 spaces** per level (the PEP 8 standard). Don't mix tabs and spaces.
- Every line in the same block must have the same indentation.
- A line ending in a colon (`:`), such as `if`, `for`, `while`, `def` or `else`, must be followed by an indented block.
- Wrong indentation causes an `IndentationError`, and the program will not run.

## Variables

A variable is a name that refers to a value. You create it by assigning with `=`. There is no need to declare its type first, because Python works it out from the value.

```python
name = "Kavya"
age = 22
```

Rules for variable names: use letters, digits and underscores, don't start with a digit, don't use Python keywords such as `if` or `class`, and remember that names are case sensitive (`age` and `Age` are different). The convention is `lowercase_with_underscores`.

## Basic Data Types

| Type | Name | Example | Description |
|---|---|---|---|
| `str` | String | `"Hello"` | Text inside quotes |
| `int` | Integer | `22` | Whole numbers |
| `float` | Float | `1.62` | Numbers with a decimal point |
| `bool` | Boolean | `True`, `False` | Logical values |

Use `type(value)` to see the type of a value:
```python
print(type(22))      # <class 'int'>
```

## Type conversion and input

`input()` always returns a **string**, even if the user types a number. To do maths with it, convert it:
```python
age = int(input("Age: "))
```
If the text isn't a valid number, `int()` raises a `ValueError`, so it should be handled with `try / except`.

## Arithmetic operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition | `17 + 5` | `22` |
| `-` | Subtraction | `17 - 5` | `12` |
| `*` | Multiplication | `17 * 5` | `85` |
| `/` | Division (always a float) | `17 / 5` | `3.4` |
| `//` | Floor division | `17 // 5` | `3` |
| `%` | Remainder | `17 % 5` | `2` |
| `**` | Power | `2 ** 3` | `8` |