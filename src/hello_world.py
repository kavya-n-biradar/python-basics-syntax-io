"""Hello World and variables: demonstrates Python's basic data types."""

# Print the classic first program
print("Hello, World!")
print()

# Variables of the four basic data types
name = "Kavya"        # str  (string): text
age = 22              # int  (integer): whole number
height = 1.62         # float: number with a decimal point
is_student = True     # bool (boolean): True or False

# Print each value together with its type, using the type() function
print("Variables and their types:")
print("name       =", name, "->", type(name))
print("age        =", age, "->", type(age))
print("height     =", height, "->", type(height))
print("is_student =", is_student, "->", type(is_student))
print()

# Basic arithmetic operations
a = 17
b = 5
print("Arithmetic with a = 17 and b = 5:")
print("Addition:       a + b  =", a + b)
print("Subtraction:    a - b  =", a - b)
print("Multiplication: a * b  =", a * b)
print("Division:       a / b  =", a / b)    # always gives a float
print("Floor division: a // b =", a // b)   # whole-number part only
print("Modulus:        a % b  =", a % b)    # remainder
print("Power:          a ** b =", a ** b)