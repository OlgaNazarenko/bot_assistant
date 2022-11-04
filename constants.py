from classes import AddressBook
from handlers import (
    hello_func,
    exit_func,
    add_contact,
    phone_сontact,
    show_all,
    add_phone,
    delete_phone,
    update_phone,
    update_birthday,

)

ADDRESS_BOOK = AddressBook()

COMMANDS = {
    'hello': hello_func,
    'good bye': exit_func,
    'phone': phone_сontact,
    'show all': show_all,
    'add_phone': add_phone,
    'add': add_contact,
    'delete_phone': delete_phone,
    'update_phone': update_phone,
    'update_birthday': update_birthday,
}
