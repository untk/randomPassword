import random
import string

class PasswordContainer:
    def __init__(self):
        self.passwords = []

    def generate_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        self.passwords.append(password)

    def save_passwords_to_file(self, filename="passwords.txt"):
        with open(filename, "w") as file:
            for i, password in enumerate(self.passwords, start=1):
                file.write(f"{i}. {password}\n")

    def display_passwords(self):
        if self.passwords:
            for i, password in enumerate(self.passwords, start=1):
                print(f"{i}. {password}")
        else:
            print("No passwords have been generated yet.")

if __name__ == "__main__":
    password_container = PasswordContainer()

    while True:
        print("1. Generate Password")
        print("2. Display Passwords")
        print("3. Save Passwords to File")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            password_length = int(input("Enter password length: "))
            if password_length < 6:
                print("Password length should be at least 6.")
            else:
                password_container.generate_password(password_length)
                print("Password generated.")
        elif choice == "2":
            password_container.display_passwords()
        elif choice == "3":
            password_container.save_passwords_to_file()
            print("Passwords saved to file.")
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
