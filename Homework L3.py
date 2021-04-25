import random

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
    print(f"Expected Result: {sampstr[0:2] + sampstr[-2:]}")

"""
Task 2

The valid phone number program.

Make a program that checks if a string is in the right format for a phone number. 
The program should check that the string contains only numerical characters and is only 10 characters long.
Print a suitable message depending on the outcome of the string evaluation.
"""


# Не модний перевіряльщик номера))
def numberchek():
    while True:
        phonumber = input("Your phone number: ")
        if phonumber.isdigit():
            if len(phonumber) == 10:
                print(f"Correct number {phonumber}")
                break
            elif len(phonumber) > 10:
                print("To long")
            elif len(phonumber) < 10:
                print("To short")
            else:
                print("The number can only be digits")


numberchek()

"""
Task 3

The name check.

Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input. 
The program should check if your input is equal to the stored name even if the given name has another case, e.g., 
if your input is “Anton” and the stored name is “anton”, it should return True.
"""

myname = "Kostia"

while True:
    mynameinpt = input("Try to guess my name: ")
    if myname.lower() == mynameinpt.lower():
        print(f"Yes my name is {myname.capitalize()}")
        break
    else:
        print(f"Sorry my name is no {mynameinpt.capitalize()}, try again.")

"""
Завдання з зірочкрою
"""


# модний перевіряльщик номера
def coolnumberchek():
    ukropercode = ["067", "096", "097", "098", "050", "066", "095", "099", "063", "073", "093"]
    while True:
        phonumber = input("Pleas, type in your cellphone number: ")
        if phonumber.isdigit():
            if phonumber[:3] in ukropercode:
                if len(phonumber) == 10:
                    break
                elif len(phonumber) > 10:
                    print("Your cellphone number to long")
                elif len(phonumber) < 10:
                    print("Your cellphone number to short")
            else:
                print(f"The cellphone number is to begin with operator code {', '.join(ukropercode)} ")
        else:
            print("The cellphone number should be inserted with digits")
    return phonumber


# Функція перевірки імені, яка провіряє чи не пусте поле.
def clientname():
    while True:
        clientnamedummy = input("Insert your first name: ")
        if clientnamedummy:
            break
        else:
            print("The first name field can't be empty")
    while True:
        clientlnamedummy = input("Insert your last name: ")
        if clientlnamedummy:
            break
        else:
            print("The last name field can't be empty")
    return clientnamedummy.capitalize() + " " + clientlnamedummy.capitalize()


# Функція можна було ще дописати самовивіз, але я не вивіз вже тай карантин нема чого лазити))
def dostavka():
    ukrdostavki = ["Nova poshta", "Meest express", "Justin", "Ukrposhta", "Delivery"]
    while True:
        dummydostavka = input("Choose a delivery company: ")
        if dummydostavka.lower() in ', '.join(ukrdostavki).lower():
            break
        else:
            print(f"Please, choose one of these ({', '.join(ukrdostavki)}) delivery services")
    while True:
        dummycity = input("Insert your city: ")
        if dummycity:
            break
        else:
            print("The field 'City' can't be empty")
    while True:
        dummystreet = input("Insert your street name: ")
        if dummystreet:
            break
        else:
            print("The field 'Street' can't be empty")
    while True:
        dummyhnumber = input("Insert your house number: ")
        if dummyhnumber:
            break
        else:
            print("The field 'House number' can't be empty")

    return dummydostavka.capitalize() + ", " + dummycity.capitalize() + ", " + dummystreet.capitalize() + ", " + dummyhnumber


# Функція яка і питає і провіряє для зручності перевірки
def ordercheck():
    positiveansv = ["yes", "y", "да", "д", "так", "т"]
    negativeansv = ["no", "n", "ні", "н", "нет"]
    clientfullname = clientname()
    clientnumber = coolnumberchek()
    clientdelivery = dostavka()
    # Check name
    while True:
        chekname = input(f"Please, confirm if your full name is {clientfullname}? ").lower()
        if chekname in negativeansv:
            chekorderstatus = input("Did you make an order in a shop 'Bananoviy Kakos'? ").lower()
            if chekorderstatus in positiveansv:
                clientfullname = clientname()
            elif chekorderstatus in negativeansv:
                print("Sorry for the inconvenience")
                break
            else:
                print("Pleas, answer Yes or No")
        elif chekname in positiveansv:
            print(f"Your full name {clientfullname} is confirmed")
        else:
            print("Pleas, answer Yes or No")

        # Check number
        while True:
            cheknumber = input(f"Please, confirm if your cellphone number is {clientnumber}? ").lower()
            if cheknumber in positiveansv:
                print(f"Your cellphone number {clientnumber} is confirmed")
                break
            elif cheknumber in negativeansv:
                clientnumber = coolnumberchek()
            else:
                print("Pleas, answer Yes or No")
        # check delivery
        while True:
            chekdelivery = input(f"Pleas, confirm if your delivery service and addresses is ({clientdelivery})? ").lower()
            if chekdelivery in positiveansv:
                print(f"Your delivery service and address information ({clientdelivery}) is confirmed")
                break
            elif chekdelivery in negativeansv:
                clientdelivery = dostavka()
            else:
                print("Pleas, answer Yes or No")
        return clientfullname + ", " + clientnumber + ", " + clientdelivery


fclientinfo = ordercheck().split(",")

print(f"\n\n{fclientinfo[0]}, your order number is №{random.randint(10000, 99999)}, "
      f"we will send a message to the number: {fclientinfo[1]}, with your track number "
      f"\nand the company '{fclientinfo[2]}' will call you an hour before it can be delivered"
      f" at the following address: {fclientinfo[3]}, {fclientinfo[4]},{fclientinfo[5]} ."
      f"\nHave a nice day and good luck!!!"
      )
