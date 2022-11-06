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
def add_contact(name: str, phone: str = None, birthday: str = None) -> str:

    if constants.ADDRESS_BOOK.get(name):
        raise ValueError("The contact details have already been added\n")

    record = Record(name, phone, birthday)
    constants.ADDRESS_BOOK.add_record(record)

    return 'The contact details have been added.'


@input_error
def add_phone(name: str, phone: str) -> str:
    contact: Record | None = constants.ADDRESS_BOOK.get(name)

    if not contact:
        raise ValueError("We cannot add the phone number to the existed one")

    contact.add_phone(phone)
    return f"The contact has been added to the list"


@input_error
def phone_сontact(name: str) -> str:
    contact = constants.ADDRESS_BOOK[name]

    phones = [str(x.value) for x in contact.phones]
    return f"{contact.name.value}: {', '.join(phones)}"


@input_error
def update_phone(name: str, old_phone: str, new_phone: str) -> str:
    contact: Record | None = constants.ADDRESS_BOOK[name]
    updated_phone = contact.update_phone(old_phone, new_phone)

    if updated_phone:
        return f"The old phone {old_phone} was updated to a new one {new_phone}."

    return f"The number {old_phone} of this person was not located in the list."


@input_error
def delete_phone(name: str, phone: str):
    contact: Record | None = constants.ADDRESS_BOOK[name]

    deleted_phone = contact.delete_phone(phone)

    if deleted_phone:
        return f"The phone number {phone} for {name} was removed."

    return f"The number {phone} of this person was not located in the list."


@input_error
def update_birthday(name: str, birthday: str) -> str:
    contact: Record | None = constants.ADDRESS_BOOK[name]

    # in Record class, method change_birthday?
    contact.change_birthday(birthday)
    return f"The birthday of this person, {name}, was change to {contact.birthday.value}"


@input_error
def days_to_birthday(name: str) -> str:
    contact: Record | None = constants.ADDRESS_BOOK[name]

    days = contact.days_to_birthday()

    if not days:
        return f"There is no data of the birthday"

    return f"It is left {days} till the next birthday of {name}"


@input_error
def show_all() -> str:

    format_contacts = []

    for contact in constants.ADDRESS_BOOK.iterator(1):
        contact = contact[0]
        phones = [str(x.value) for x in contact.phones]
        birthday = contact.birthday.value if contact.birthday else ''
        contact = f"{contact.name.value} : {birthday} : {', '.join(phones)}"

        format_contacts.append(contact)

    return '\n'.join(format_contacts)
