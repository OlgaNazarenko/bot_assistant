from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.value = value
    #     check_phone(value)

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
        phone = Phone(phone)

        if any(x.value == phone.value for x in self.phones):
            return self.phones.append(phone)
        return phone

    def delete_phone(self, phone):
        for phone in self.phone:
            if phone.value == phone:
                self.phone.remove(phone)
                return phone

    def update_phone(self, old_phone, new_phone):
        for phone in self.phone:
            if phone.value == old_phone:
                self.update(new_phone)
                return new_phone


class AddressBook(UserDict):

    def add_record(self, record):

        contact = Record(name=Name, phone=Phone)
        self.data[record.name.value] = contact
