
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    for c in contacts.keys():
        if c == name:
            contacts[c] = phone
            return f'Contact with name {c} changed to {phone}'
    return "Contact not found"

def show_phone(name, contacts):
    for c in contacts.keys():
        if c == name:
            return f'{c} : {contacts[c]}'
    return "Contact not found"

def show_all(contacts):
    result = ''
    count = 0
    for c in contacts.keys():
        count+=1
        result += c + " : " + contacts[c] + ";"
        if len(contacts.keys()) != count:
            result += "\n"
    return result

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip().lower()
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
            print(show_phone(args[0], contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()