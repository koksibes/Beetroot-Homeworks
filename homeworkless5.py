import random
"""
Task 1

The greatest number

Write a Python program to get the largest number from a list of random numbers with the length of 10

Constraints: use only while loop and random module to generate numbers
"""

numbers = []
a=0
while len(numbers)<=10:
    numbers.append(random.randint(0, 1000))
b=numbers[0]
print(numbers)
while a<len(numbers)-1:
    if b<numbers[a+1]:
        b = numbers[a + 1]
    a += 1


print(f"Найбольшее значение {b}")
"""
Task 2

Exclusive common numbers.

Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common 
integers between the 2 initial lists without any duplicates.

Constraints: use only while loop and random module to generate numbers
"""
numbers1=[]
while len(numbers1)<=10:
    numbers1.append(random.randint(0, 10))
numbers2=[]
while len(numbers2)<=10:
    numbers2.append(random.randint(0, 10))

numberssum=list(set(numbers1)- set(numbers2))

print(f"Список {numberssum}")
"""
Task 3

Extracting numbers.

Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but
 not a multiple of 5, and store them in a separate list. Finally, print the list.

Constraint: use only while loop for iteration
"""
liststo=list(range(1,101))
i=0
listsev=[]
while i<len(liststo):
    if liststo[i]%7==0 and liststo[i]%5 != 0:
        listsev.append(liststo[i])
    i+=1
print(listsev)
