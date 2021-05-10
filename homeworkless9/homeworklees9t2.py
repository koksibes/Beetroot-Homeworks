import json
from json.decoder import JSONDecodeError

# Code for add new entries
"""
Extend Phonebook application

Functionality of Phonebook application:

Add new entries
Search by first name
Search by last name
Search by full name
Search by telephone number
Search by city or state
Delete a record for a given telephone number
Update a record for a given telephone number
An option to exit the program


The first argument to the application should be the name of the phonebook. Application should load JSON data,
 if it is present in the folder with application,else raise an error.
 After the user exits, all data should be saved to loaded JSON.

"""


def get_number():
    while True:
        phonenumber = input("Insert phone number: ")
        if phonenumber.isdigit():
            return {"phone": phonenumber}
        else:
            print("The number can only be digits")


def get_firstname():
    firstname = input("Insert first name: ")
    return {"firstname": firstname}


def get_lastname():
    lastname = input("Insert last name: ")
    return {"lastname": lastname}


def get_fullname(firstname, lastname):
    fullname = firstname["firstname"] + " " + lastname["lastname"]
    return {"fullname": fullname}


def get_email():
    contact_email = input("Insert Email: ")
    return {"contact_email": contact_email}


def add_contact():
    firstname = get_firstname()
    lastname = get_lastname()
    fullname = get_fullname(firstname, lastname)
    phonenumber = get_number()
    contact_email = get_email()
    contact = {}
    contact.update(firstname)
    contact.update(lastname)
    contact.update(fullname)
    contact.update(phonenumber)
    contact.update(contact_email)
    return contact


def store_contact():
    contact = add_contact()
    with open("phonebook.json") as fp_to_read:
        try:
            contact_storage = json.load(fp_to_read)
            with open("phonebook.json", "w") as fp_to_write:
                contact_to_apend = {str(len(contact_storage) + 1): contact}
                contact_storage.update(contact_to_apend)
                json.dump(contact_storage, fp_to_write, sort_keys=True, indent=4)
        except JSONDecodeError:
            contact_to_apend = {1: contact}
            with open("phonebook.json", "w") as fp_to_write:
                json.dump(contact_to_apend, fp_to_write, sort_keys=True, indent=4)


store_contact()
