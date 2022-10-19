import inspect
from functools import wraps
from types import FunctionType
import re
from utils import input_error
from classes import Record
from constants import ADDRESS_BOOK

CONTACTS: dict[str, dict[str, int]] = {}


@input_error
def hello_func():
    return 'How can I help you?'


@input_error
def exit_func():
    return 'Good bye!'


@input_error
def add_contact(name: str, phone: str) -> str:

        pattern = r"(^380|0|80)\d{9}$"
        match = re.fullmatch(pattern, phone)
        if not match:
            return "Invalid, please enter a valid phone number"


        if CONTACTS.get(name):
            raise ValueError("The contact details have already been added\n")

        # CONTACTS.update({name: {"name": name, "phone": phone}})

        record = Record(name)
        record.add_phone(phone)
        ADDRESS_BOOK.add_record(record)

        return 'The contact details have been added.'

@input_error
def phone_сontact(name: str, phone: str) -> str:
    name, phone = add_contact(name, phone)
    record_add = add_phone(phone)
    ADDRESS_BOOK.add_record(record_add)

    # return CONTACTS[name]["phone"]

def validate_phone(phone: str):
    result = re.search(r"(^380|0|80)\d{9}$", CONTACTS[phone])


    if not result:
        raise ValueError(f'The phone number is invalid, {phone}.')


@input_error
def change_contact(name: str, old_phone: str, new_phone: str) -> str:

    name, phone = add_contact(name,new_phone)

    if new_phone:
        pattern = r"(^380|0|80)\d{9}$"
        match = re.fullmatch(pattern, new_phone)
        if match:
            print("Valid")
        else:
            raise ValueError("Invalid phone number")


    # CONTACTS[name]['phone'] = new_phone
    record = Record(name)
    record.add_phone(new_phone)
    ADDRESS_BOOK.add_phone(record)

    return f'The phone number for {name} was changed from {old_phone} to {new_phone}. ' \
           f'And it is updated in the main file.'


@input_error
def show_all() -> str:
    return f'All contacts can be seen in: \n{ADDRESS_BOOK.data}'

    ADDRESS_BOOK = []
    # format_contacts = []

    for contact in CONTACTS.values():
        contact = f"{contact['name']}: {contact['phone']}"

        ADDRESS_BOOK.append(contact)

    return '\n'.join(ADDRESS_BOOK)