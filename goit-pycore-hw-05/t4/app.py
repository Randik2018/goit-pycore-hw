def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command"
        except KeyError:
            return "Contact not found"
        except IndexError:
            return "Enter the argument for the command"

    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f'Contact with name {name} changed to {phone}'
    else:
        raise KeyError

@input_error
def show_phone(args, contacts):
    name = args[0]
    return f'{name.title()} : {contacts[name]}'



def show_all(contacts):
    if not contacts:
        return 'no contacts yet...'
    return '\n'.join(f'{k.title()}: {v}' for k, v in contacts.items())


@input_error
def parse_input(user_input):
    cmd, *args = user_input.strip().lower().split()
    return cmd, *args


def main():
    # contacts = {'ann': '123', 'bob': '456'}
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
