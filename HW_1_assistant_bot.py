# parser
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# adding new contact
def add_contact(args, contacts):
    name, phone = args
    name = name.lower()
    contacts[name] = phone
    return "Contact added."

# rewriting new phone
def change_contact(args, contacts):
    name, new_phone = args
    name = name.lower()
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."

# show phone number
def show_phone(args, contacts):
    name = args[0].lower()
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

# get all contacts
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    else:
        contacts_list = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
        return contacts_list

# request-response cycle
def main():
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
        elif command == "add" and len(args) == 2:
            print(add_contact(args, contacts))
        elif command == "change" and len(args) == 2:
            print(change_contact(args, contacts))
        elif command == "phone" and len(args) == 1:
            print(show_phone(args, contacts))
        elif command == "all" and not args:
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

    