from collections import UserDict
from utils import check_phone

class Field:
    def __int__(self, value):
        self.value = value


class Name(Field):
    pass

class Phone(Field):
    def __int__(self, value):
         self.value = check_phone(value)


class Record(Field):
    def __init__(self, name, phone):
        self.name = Name(name)
        self.phone = []

    def add_phone(self,phone):
        self.phone.append(phone)


    def delete_phone(self,phone):
        for phone in self.phone:
            if phone.value == phone:
                self.phone.remove(phone)
                return phone

    def update_phone(self,old_phone,new_phone):
        for phone in self.phone:
            if phone.value == old_phone:
                self.update(new_phone)
                return new_phone

class AddressBook(UserDict):

    def add_record(self,name,phone):

        if self.data.get(name):
            raise ValueError("The contact details have already been added\n")

        contact = Record(name=name,phone=phone)
        self.data[record.name.value] = contact
