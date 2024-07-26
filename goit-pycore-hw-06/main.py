from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if not self.validate_phone(value):
            raise ValueError("Phone number must be 10 digits")
        super().__init__(value)

    @staticmethod
    def validate_phone(value):
        return bool(re.match(r'^\d{10}$', value))


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                self.remove_phone(old_phone)
                self.add_phone(new_phone)
                return
        raise ValueError("Phone number not found")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        if not isinstance(record, Record):
            raise TypeError("Must add a Record instance")
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError(f"Record with name '{name}' not found")


# Пример использования
if __name__ == "__main__":
    # Создание новой адресной книги
    book = AddressBook()

    # Создание записи для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Добавление записи John в адресную книгу
    book.add_record(john_record)

    # Создание и добавление нового записи для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Вывод всех записей в книге
    for name, record in book.data.items():
        print(record)

    # Поиск и редактирование телефона для John
    john = book.find("John")
    if john:
        john.edit_phone("1234567890", "1112223333")
        print(john)  # Вывод: Contact name: John, phones: 1112223333; 5555555555

        # Поиск конкретного телефона в записи John
        found_phone = john.find_phone("5555555555")
        print(f"{john.name}: {found_phone}")  # Вывод: 5555555555

    # Удаление записи Jane
    book.delete("Jane")