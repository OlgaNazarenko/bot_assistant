import json
from json import JSONEncoder
from json import JSONDecoder
import re
from collections import UserDict
import constants
from datetime import date
from typing import Generator
import os


class Field:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __repr__(self):
        return f"{self.__class__.__name__}(value={self.value})"


class Name(Field):
   pass


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.value = value

    @Field.value.setter
    def value(self, value):
        self._value = self.check_phone(value)

    @staticmethod
    def check_phone(phone: str) -> str:
        pattern = r"(^380|0|80)\d{9}$"
        match = re.fullmatch(pattern, phone)
        if not match:
            raise ValueError("Invalid, please enter a valid phone number")

        return phone


class Birthday(Field):
    def __init__(self, value: str):
        super().__init__(value)
        self.value: date = value

    @Field.value.setter
    def value(self, value: str):
        self._value = self._check_birthday(value)

    @staticmethod
    def _check_birthday(_date: str) -> date:
        try:
            day, month, year = _date.split('.')
        except IndexError:
            raise ValueError("Invalid date format. Date format should be DD.MM.YYYY.")

        return date(int(year), int(month), int(day))


class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name: Name = Name(name)
        self.birthday = Birthday(birthday) if birthday else ''
        self.phones: list[Phone, ...] = [Phone(phone)] if phone else []

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

    def change_birthday(self, birthday: str) -> Birthday:
        self.birthday = Birthday(birthday)
        return self.birthday

    def days_to_birthday(self) -> int | None:
        if not self.birthday:
            return

        birthday = self.birthday.value
        today = date.today()

        if (birthday.month >= today.month) and (birthday.day >= today.day):
            birthday = birthday.replace(year=today.year)

        elif birthday.month <= today.month:
            birthday = birthday.replace(year=today.year + 1)

        return (birthday - today).days

    def __repr__(self):
        return "Record({})".format(', '.join([f"{k}={v!r}" for k, v in self.__dict__.items()]))


class AddressBook:

    def __init__(self):
        self.file_name = "common_contacts.json"
        open(self.file_name, 'a').close()

    def add_record(self, record: Record):
        contact = {
            'name': record.name.value,
            'phones': [x.value for x in record.phones],
            'birthday': record.birthday.value.strftime('%d.%m.%Y') if record.birthday else None
        }

        with open(self.file_name, 'a') as file:
            contact = json.dumps(contact)
            file.write(contact + '\n')

    def iterator(self, count: int) -> 'Generator[list[Record, ...]]':
        contacts_iteration = []

        for contact in self.__read_file():
            contacts_iteration.append(contact)

            if len(contacts_iteration) >= count:
                yield contacts_iteration
                contacts_iteration = []

        if contacts_iteration:
            yield contacts_iteration

    def __read_file(self) -> 'Generator[Record]':
        with open(self.file_name, 'r') as file:
            for line in file:
                contact = json.loads(line)
                record = Record(contact['name'])
                record.birthday = Birthday(contact['birthday']) if contact['birthday'] else ''
                record.phones = [Phone(x) for x in contact['phones']]
                yield record

    def search_contacts(self, value: str) -> list[Record, ...] | None:
        found_contacts = []

        for contact in self.__read_file():
            if value in contact.name.value or any(value in str(phone.value) for phone in contact.phones):
                found_contacts.append(contact)

        if found_contacts:
            return found_contacts

    def get_contact(self, name: str) -> Record | None:
        for contact in self.__read_file():
            if name == contact.name.value:
                return contact

    # This additional and temporary command was created because all data here is saved in the file, and it is impossible 
    # to change object in this format.
    def change_contact(self, contact: Record, remove: bool = False) -> None:
        temporary_filename = 'old_contacts.json'

        os.rename(self.file_name, temporary_filename)

        self.file_name = temporary_filename

        for _contact in self.__read_file():
            if _contact.name.value == contact.name.value:
                if remove:
                    continue

                AddressBook().add_record(contact)

            else:
                AddressBook().add_record(_contact)

        os.remove(temporary_filename)
        self.file_name = AddressBook().file_name

    def __getitem__(self, item):
        for contact in self.__read_file():
            if item == contact.name.value:
                return contact
        else:
            raise KeyError(item)


if __name__ == '__main__':
    c = AddressBook()
    c.add_record(Record('Apple', '', '22.10.2000'))
    c.add_record(Record('Sugar', '0931111212', ''))
    c.add_record(Record('Salt', '0931111212', '22.10.2000'))
    for x in c.iterator(1):
        print(x)
