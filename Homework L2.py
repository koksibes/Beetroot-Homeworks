"""
Task 1

The greeting program.

Make a program that has your name and the current day of the week stored as separate variables and
 then prints a message like this:

     “Good day <name>! <day> is a perfect day to learn some python.”

Note that <name> and <day> are predefined variables in source code.

An additional bonus will be to use different string formatting methods for constructing result string.

"""

name = input(" What's your name? ")
day = input(" What day is today? ")
print(f'Good day {name.capitalize()}! {day.capitalize()} is a perfect day to learn some python')

"""
Task 2

Manipulate strings.

Save your first and last name as separate variables,
then use string concatenation to add them together with a white space in between and print a greeting.
"""
#We get name from the first task
lastname = input("What's your lastname? ")
fullname = name.capitalize() + " " + lastname.capitalize()
print(f"Hello, {fullname}")

"""
Task 3

Using python as a calculator.

Make a program with 2 numbers saved in separate variables a and b, then print the result for each of the following: 

Addition
Subtraction
Division
Multiplication
Exponent (Power)
Modulus
Floor division
"""

a = int(input("Input number a: "))
b = int(input("Input number b: "))
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Division: {a / b}")
print(f"Multiplication: {a * b}")
print(f"Exponent (Power): {a ** b}")
print(f"Modulus: {a % b}")
print(f"Floor division: {a // b}")
