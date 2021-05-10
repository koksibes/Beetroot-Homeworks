"""
    Task 1

    Write a function called oops that explicitly raises an IndexError exception when called.
    Then write another function that calls oops inside a try/except statement to catch the error.
    What happens if you change oops to raise KeyError instead of IndexError?
"""
test_list1 = [i for i in range(10)]


def oops(test_list):

    try:
        i = 10
        while i <= len(test_list):
            test_list[i] = test_list[i] ** 2
            i += 1
            return test_list
    except IndexError:
        return "Sorry"


print(oops(test_list1))

"""
Task 2

    Write a function that takes in two numbers from the user via input(), 
    call the numbers a and b, and then returns the value of squared a 
    divided by b, construct a try-except block which raises an exception if the two values
    given by the input function were not numbers, and if value b was zero (cannot divide by zero).    
"""
