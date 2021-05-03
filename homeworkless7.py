"""
Task 1

A simple function.

Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.
The function should then print “My favorite movie is named {name}”.

"""

"""
def favorite_movie():
    movie_name = input("Insert the name of your favorite movie: ")
    print(f"My favorite movie is named '{movie_name}'")


favorite_movie()
"""

"""
Task 2

Creating a dictionary.

Create a function called make_country, which takes in a country’s name and capital as parameters.
Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter.
Make the function print out the values of the dictionary to make sure that it works as intended.
"""
countrys = ["Ukraine", "France", "Italy", "China", "Canada"]
capitals = ["Kiev", "Paris", "Rome", "Bejing", "Ottawa"]


def make_country(country, capital):
    country_dict = {}
    for i, j in zip(country, capital):
        country_dict.update({i: j})
    return country_dict


print(make_country(countrys, capitals))

"""
Task 3

A simple calculator.

Create a function called make_operation, 
which takes in a simple arithmetic operator as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) 
and an arbitrary number of arguments (only numbers) as the second parameter. 
Then return the sum or product of all the numbers in the arbitrary parameter. For example:

the call make_operation(‘+’, 7, 7, 2) should return 16
the call make_operation(‘-’, 5, 5, -10, -20) should return 30
the call make_operation(‘*’, 7, 6) should return 42  

"""


def calculator(a, *args):
    result = 0
    if a == "+":
        for i in args:
            result += i
    elif a == "-":
        for i in args:
            result -= i
    elif a == "*":
        result=1
        for i in args:
            result *= i
    return result



calculator("/", 5, 5, -10, -20)
