# Python Basics: Syntax, Variables and Input/Output

A beginner Python project for the CodeMore Python Programming Internship (Week 1, Task 4). It covers Python syntax, indentation, variables, data types and basic input/output.

## Project Overview

- `src/hello_world.py` declares variables of different data types, prints their values and types, and shows basic arithmetic.
- `src/user_input.py` asks for the user's name, age and favorite programming language, prints a personalized greeting and calculates the year they will turn 100.
- `docs/syntax_notes.md` explains indentation and data types in more detail.

## Project Structure

```
python-basics-syntax-io/
├── README.md
├── .gitignore
├── src/
│   ├── hello_world.py
│   └── user_input.py
└── docs/
    ├── syntax_notes.md
    └── screenshots/
```

## Setup and How to Run

1. Install Python 3.8 or newer from python.org (tick "Add Python to PATH") and check it with `python --version`.
2. Clone the repository:
```bash
   git clone https://github.com/kavya-n-biradar/python-basics-syntax-io.git
   cd python-basics-syntax-io
```
3. Run the scripts:
```bash
   python src/hello_world.py
   python src/user_input.py
```

## Python Syntax Rules Learned

- **Indentation defines blocks.** Python uses 4 spaces per level, and a line ending with `:` must be followed by an indented block.
- **Variables need no type declaration.** The type comes from the value assigned.
- **Basic types:** `str`, `int`, `float` and `bool`, which can be checked with `type()`.
- **`input()` always returns a string,** so it must be converted with `int()` or `float()` before doing maths.
- **Invalid input should be handled,** for example with `try / except ValueError` and loops that ask again.
- **Comments start with `#`,** and docstrings in triple quotes describe functions and files.
- **Arithmetic operators:** `+ - * / // % **`. Note that `/` always gives a float.

## Console Output

### `hello_world.py`
```
Hello, World!

Variables and their types:
name       = Kavya -> <class 'str'>
age        = 22 -> <class 'int'>
height     = 1.62 -> <class 'float'>
is_student = True -> <class 'bool'>

Arithmetic with a = 17 and b = 5:
Addition:       a + b  = 22
Subtraction:    a - b  = 12
Multiplication: a * b  = 85
Division:       a / b  = 3.4
Floor division: a // b = 3
Modulus:        a % b  = 2
Power:          a ** b = 1419857
```

### `user_input.py`
```
What is your name? Kavya
How old are you? 22
What is your favorite programming language? Python

Hello, Kavya! Nice to meet you.
Python is a great choice. Keep coding!
You will turn 100 in the year 2104.
```

Screenshots of both runs are in [`docs/screenshots/`](docs/screenshots/).

## What I Learned

- How Python's indentation replaces curly braces and why consistent spacing matters
- How to create variables and check data types with `type()`
- How to read user input, convert it and validate it
- How to format output with f-strings
- How to document a project with a README and notes

## Author

Kavya Biradar