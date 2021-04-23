"""
Task 1

String manipulation

Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
If the string length is less than 2, return instead of the empty string.

Sample String: 'helloworld'

Expected Result : 'held'

Sample String: 'my'

Expected Result : 'mymy'

Sample String: ' x'

Expected Result: Empty String

Tips:

Use built-in function len() on an input string
Use positive indexing to get the first characters of a string and negative indexing to get the last characters
"""
sampstr = input("Input sample string: ")
if len(sampstr) < 2:
    print("Expected Result: Empty String")
else:
    print(f"Expected Result: {sampstr[0:2]+sampstr[-2:]}")

"""
Task 2

The valid phone number program.

Make a program that checks if a string is in the right format for a phone number. 
The program should check that the string contains only numerical characters and is only 10 characters long.
Print a suitable message depending on the outcome of the string evaluation.
"""

phonumber = input("Your phone number: ")
if phonumber.isdigit():
    if len(phonumber) == 10:
        print(f"Correct number {phonumber}")
    elif len(phonumber) > 10:
        print("To long")
    elif len(phonumber) < 10:
        print("To short")
else:
    print("The number can only be digits")

"""
Task 3

The name check.

Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input. 
The program should check if your input is equal to the stored name even if the given name has another case, e.g., 
if your input is “Anton” and the stored name is “anton”, it should return True.
"""
myname = "Kostia"
mynameinpt = input("Try to guess my name: ")
if myname.lower() == mynameinpt.lower():
    print(f"Yes my name is {myname}")
else:
    print(f"Sorry my name is no {mynameinpt.capitalize()}, try again.")
