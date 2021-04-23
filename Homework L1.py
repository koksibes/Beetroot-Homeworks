""""
Task 1

Run the python interpreter via the terminal. Get familiar with running python commands in the terminal,
 work with output, etc.
"""

print('Hello Teacher i am install python')

"""
Task 2
Create a python program named “task2”, and use the built-in function `print` in it several times. Try to pass “sep”, 
“end” params and pass several parameters separated by commas. 

Also, provide a comment text above each print statement, mentioned above,
 with the expected output after execution of the particular print statement.

(Ex.
# ‘hello world’
print(“hello world”)
)
"""
#sep
batman = ["B","a","t","m","a","n"]
print( *batman , sep=",")

#end
print( *batman , sep='', end=" Is a Greater Hero")

"""
Task 3

Write a program, which has two print statements to print the following text
 (capital letters “O” and “H”, made from “#” symbols):

#########
#       #
#       #
#       #
#########

#       #
#       #
######### 
#       # 
#       #
Pay attention that usage of spaces is forbidden, as well as creating the whole result text string using “”” ”””
, use ‘\n’ and ‘\t’ symbols instead.

"""
#Letter:O

line = "\n"+"#"*9
two_dot = "\n#"+"\t"*2+"#"
print(line+two_dot*3+line)

#Letter:H
print(two_dot*2+line+two_dot*2)
