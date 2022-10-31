from classes import AddressBook
from handlers import (
    hello_func,
    exit_func,
    add_contact,
    phone_сontact,
    change_contact,
    show_all
)
ADDRESS_BOOK = AddressBook()

COMMANDS = {
    'hello': hello_func,
    'good bye': exit_func,
    'add': add_contact,
    'phone': phone_сontact,
    'change': change_contact,
    'show all': show_all
}
