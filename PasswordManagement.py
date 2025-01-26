from cryptography.fernet import Fernet
import os


def generate_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
        print("Key generated and saved to key.key")

# Load the key from the file
def load_key():
    return open("key.key", "rb").read()

# Encrypt a password
def encrypt_password(password, key):
    fernet = Fernet(key)
    return fernet.encrypt(password.encode()).decode()

# Decrypt a password
def decrypt_password(encrypted_password, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_password.encode()).decode()

# Save a password
def save_password(website, username, password):
    key = load_key()
    encrypted_password = encrypt_password(password, key)
    with open("passwords.txt", "a") as file:
        file.write(f"{website},{username},{encrypted_password}\n")
    print(f"Password saved for {website}!")

# Retrieve passwords
def retrieve_passwords():
    key = load_key()
    if not os.path.exists("passwords.txt"):
        print("No saved passwords found.")
        return
    with open("passwords.txt", "r") as file:
        for line in file:
            website, username, encrypted_password = line.strip().split(",")
            password = decrypt_password(encrypted_password, key)
            print(f"Website: {website}, Username: {username}, Password: {password}")

# Main menu
def menu():
    print("==== Password Manager ====")
    print("1. Save a new password")
    print("2. Retrieve passwords")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice

# Main program
if __name__ == "__main__":
    if not os.path.exists("key.key"):
        generate_key()

    while True:
        choice = menu()
        if choice == "1":
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            save_password(website, username, password)
        elif choice == "2":
            retrieve_passwords()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
