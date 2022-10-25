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
    name, phone = create_data(name, phone)
    record = Record(phone)

    return f"'name:'{constants.ADDRESS_BOOK.data[name].name.value}, 'phone:'{list(map(lambda x: x.value, constants.ADDRESS_BOOK.data[name].phones))}"
 


def validate_phone(phone: str):
    result = re.search(r"(^380|0|80)\d{9}$", constants.ADDRESS_BOOK[phone])

    if not result:
        raise ValueError(f'The phone number is invalid, {phone}.')


@input_error
def change_contact(name: str, old_phone: str, new_phone: str) -> str:
    name, phone = create_data(name, old_phone)

    record = Record(name)
    record.add_phone(new_phone)
    constants.ADDRESS_BOOK.add_record(record)

    return f'The phone number for {name} was changed from {old_phone} to {new_phone}. ' \
           f'And it is updated in the main file.'


@input_error
def show_all() -> str:
    return f'All contacts can be seen in: \n{constants.ADDRESS_BOOK}'

    constants.ADDRESS_BOOK = []

    for contact in constants.ADDRESS_BOOK.values():
        contact = f"{contact['name']}: {contact['phone']}"

        constants.ADDRESS_BOOK.append(contact)

    return '\n'.join(constants.ADDRESS_BOOK)


def create_data(name: str, phone: str):
    name = name[0]
    phone = phone[1]
    if name.isnumeric():
        raise ValueError('You entered a wrong name.')
    if not phone.isnumeric():
        raise ValueError('You entered a wrong phone number.')
    return name, phone


@input_error
def delete_func(name: str, phone: str):
    name, phone = create_data(data)
    record_delete = addressbook.data[name]

    if record_delete.delete_phone(phone) is True:
        return f'Contact name: {name} phone: {phone}, has been deleted.'
    else:
        return 'The entered phone number does not exist'
