import re
from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.__class__.__name__}(value={self.value})"


class Name(Field):
   pass


class Phone(Field):
    def __init__(self, value):
        value = self.check_phone(value)

        super().__init__(value)
        self.value = value

    @staticmethod
    def check_phone(phone: str) -> str:
        pattern = r"(^380|0|80)\d{9}$"
        match = re.fullmatch(pattern, phone)
        if not match:
            raise ValueError("Invalid, please enter a valid phone number")

        return phone


class Record:
    def __init__(self, name, phone=None):
        self.name = Name(name)
        self.phones = [Phone(phone)] if phone else []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def delete_phone(self, phone: str) -> str | None:
        for phone_ in self.phones:
            if phone_.value == phone:
                self.phones.remove(phone_)
                return phone

    def update_phone(self, old_phone: str, new_phone: str) -> str | None:
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return new_phone

    def __repr__(self):
        return "Record({})".format(', '.join([f"{k}={v!r}" for k, v in self.__dict__.items()]))


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record
