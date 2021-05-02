"""
Task 1

Make a program that has some sentence (a string) on input and
returns a dict containing all unique words as keys and the number of occurrences as values.
"""
usersmpltxt = "I am happy with my happy life, family, and friends!"


def cleartext(usertext):
    punktmark = [",", ":", ";", ".", "?", "!", "..."]
    for pmark in punktmark:
        if pmark in usertext:
            usertext = usertext.replace(pmark, "")
    if " - " in usertext:
        usertext = usertext.replace(" - ", " ")
    return usertext.lower()


listwords = cleartext(usersmpltxt).split()

dictwords = {}
for i in listwords:
    dictwords[i] = listwords.count(i)
print(dictwords)
"""
Task 2

Input data:

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3

Create a function which takes as input two dicts with structure mentioned above,
 then computes and returns the total price of stock.
"""
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


def shop(stocks, price):
    check = {}
    for key in stocks:
        if key in prices and stocks[key] != 0:
            check[key] = stocks[key] * price[key]
    check["total"] = sum(check.values())
    return check


def printchek(check):
    for key in check:
        print(f"{key.capitalize()}: {check[key]} UAH")


printchek(shop(stock, prices))
"""
Task 3

List comprehension exercise

Use a list comprehension to make a list containing tuples (i, j) 
where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.
"""
squadlist = [(i, i ** 2) for i in range(1, 11)]
print(squadlist)
"""
создать словарь месяц:номер и перевернуть его компрехеншеном   номер:месяц   или для дня недели.
"""
import calendar

month_dict = {}
for month_idx in range(1, 13):
    month_dict[calendar.month_name[month_idx]] = month_idx

month_dictreversed = {month_dict[i]: i for i in month_dict}
print(month_dict)
print(month_dictreversed)
