"""
Task 1

The Guessing Game.
Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
The result should be sent back to the user via a print statement.

"""
"""
import random
guessednumber = random.randint(0, 10)
trynumber = int(input("Try to guess my number "))
if guessednumber == trynumber:
    print(f"Yes my nymber is {guessednumber}")
else:
    print(f"No my nymber is {guessednumber}, maybe next time")
"""
"""
Task 2

The birthday greeting program.

Write a program that takes your name as input, and then your age as input and greets you with the following:

“Hello <name>, on your next birthday you’ll be <age+1> years”   
"""
"""
name = input("What's your name? ")
age = input("How old are you? ")
print(f"Hello {name.capitalize()}, on your next birthday you’ll be {int(age) + 1} years")
"""
"""
Task 3


Words combination

Create a program that reads an input string and then creates and 
prints 5 random strings from characters of the input string.

For example, the program obtained the word ‘hello’, 
so it should print 5 random strings(words) that combine characters 
‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …

Tips: Use random module to get random char from string)
"""
import random
c=random.choice("hello")
print(c)
"""
Task 4

The math quiz program

Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, 
and then responds with a message accordingly.
"""
#