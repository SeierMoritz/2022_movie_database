from database import add_entry, entries

def prompt_new_entry():
    entry_content = input("What have you learned today? ")
    entry_date = input("Enter the date: ")

    add_entry(entry_content, entry_date)


def view_entries(entries):
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")

menu = """Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: """
welcome = "Welcome to the programming diary!"

user_input = input(menu)
while (user_input := input(menu)) != "3":
    if user_input == "1":
        print("Adding...")
        prompt_new_entry()
    elif user_input == "2":
        print("Viewing...")
        view_entries(entries)
    else:
        print("Invalid option, please try again!")
