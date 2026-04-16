import os
import webbrowser


def open_websites():
    print("Opening your favorite websites...")
    try:
        file = open("favorite_websites.txt", "r")
        websites = file.readlines()
        file.close()

        if len(websites) == 0:
            print("You have no saved websites. Please add some first!")
        else:
            for site in websites:
                clean_site = site.strip()
                if clean_site != "":
                    webbrowser.open(clean_site)
            print("Websites opened!")
    except FileNotFoundError:
        print("You have no saved websites. Please add some first!")


def open_notepad():
    print("Opening Notepad...")
    # os.startfile is a Windows-specific command to open programs
    os.startfile("notepad.exe")
    print("Notepad opened!")


def open_calculator():
    print("Opening Calculator...")
    os.startfile("calc.exe")
    print("Calculator opened!")


def add_website():
    print("Please enter the website URL (e.g. https://www.reddit.com):")
    website = input("> ")
    file = open("favorite_websites.txt", "a")
    file.write(website + "\n")
    file.close()
    print("Successfully added " + website + "!")


def take_note():
    print("What would you like to note down?")
    note = input("> ")
    file = open("my_notes.txt", "a")
    file.write("- " + note + "\n")
    file.close()
    print("Note saved to 'my_notes.txt'!")


def show_notes():
    print("--- Your Notes ---")
    try:
        file = open("my_notes.txt", "r")
        content = file.read()
        print(content)
        file.close()
    except FileNotFoundError:
        print("You don't have any notes yet!")
    print("------------------")


def main():
    print("Welcome to Your Personal PC Assistant!")

    while True:
        print("\n--- Main Menu ---")
        print("1. Open my favorite websites")
        print("2. Add a favorite website")
        print("3. Open Notepad")
        print("4. Open Calculator")
        print("5. Take a quick note")
        print("6. Show my notes")
        print("7. Exit")

        choice = input("Enter a number (1-7): ")

        if choice == "1":
            open_websites()
        elif choice == "2":
            add_website()
        elif choice == "3":
            open_notepad()
        elif choice == "4":
            open_calculator()
        elif choice == "5":
            take_note()
        elif choice == "6":
            show_notes()
        elif choice == "7":
            print("Hope you have a great day. Goodbye!")
            break
        else:
            print("That option doesn't exist, sorry :(")


if __name__ == "__main__":
    main()
