import inspect
from functools import wraps
from types import FunctionType
import re
from utils import input_error
from classes import Record
import constants


@input_error
def hello_func():
    return 'How can I help you?'


@input_error
def exit_func():
    return 'Good bye!'


@input_error
def add_contact(name: str, phone: str) -> str:

    if constants.ADDRESS_BOOK.get(name):
        raise ValueError("The contact details have already been added\n")

    record = Record(name)
    record.add_phone(phone)
    constants.ADDRESS_BOOK.add_record(record)

    return 'The contact details have been added.'


@input_error
def phone_сontact(name: str, phone: str) -> str:
    name, phone = add_contact(name, phone)
    record_add = add_phone(phone)
    constants.ADDRESS_BOOK.add_record(record_add)


def validate_phone(phone: str):
    result = re.search(r"(^380|0|80)\d{9}$", constants.ADDRESS_BOOK[phone])

    if not result:
        raise ValueError(f'The phone number is invalid, {phone}.')


@input_error
def change_contact(name: str, old_phone: str, new_phone: str) -> str:
    name, phone = add_contact(name, new_phone)

    record = Record(name)
    record.add_phone(new_phone)
    constants.ADDRESS_BOOK.add_phone(record)

    return f'The phone number for {name} was changed from {old_phone} to {new_phone}. ' \
           f'And it is updated in the main file.'


@input_error
def show_all() -> str:
    return f'All contacts can be seen in: \n{constants.ADDRESS_BOOK.data}'

    constants.ADDRESS_BOOK = []

    for contact in constants.ADDRESS_BOOK.values():
        contact = f"{contact['name']}: {contact['phone']}"

        constants.ADDRESS_BOOK.append(contact)

    return '\n'.join(constants.ADDRESS_BOOK)
