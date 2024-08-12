import pickle

class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, address):
        self.contacts[name] = address

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

    def get_contact(self, name):
        return self.contacts.get(name, "Контакт не найден")

    def list_contacts(self):
        return self.contacts

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Возвращаем новую адресную книгу, если файл не найден

def main():
    # Загружаем адресную книгу из файла при запуске программы
    book = load_data()

    while True:
        command = input("Введите команду (add, remove, get, list, exit): ")

        if command == "add":
            name = input("Введите имя: ")
            address = input("Введите адрес: ")
            book.add_contact(name, address)
        elif command == "remove":
            name = input("Введите имя: ")
            book.remove_contact(name)
        elif command == "get":
            name = input("Введите имя: ")
            print(book.get_contact(name))
        elif command == "list":
            contacts = book.list_contacts()
            for name, address in contacts.items():
                print(f"{name}: {address}")
        elif command == "exit":
            # Сохраняем адресную книгу в файл перед выходом из программы
            save_data(book)
            print("Адресная книга сохранена. Выход из программы.")
            break
        else:
            print("Неизвестная команда. Попробуйте еще раз.")

if __name__ == "__main__":
    main()