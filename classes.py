import re
from collections import UserDict
import constants
from datetime import date


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
#represents the name of the class


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
    def __init__(self, value):
        super().__init__(value)
        self.value = value

    @Field.value.setter
    def value(self, value):
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


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def iterator(self, count: int):
        contacts_iteration = []

        for contact in self.data.values():
            contacts_iteration.append(contact)

            if len(contacts_iteration) >= count:
                yield contacts_iteration
                contacts_iteration = []

        if contacts_iteration:
            yield contacts_iteration
