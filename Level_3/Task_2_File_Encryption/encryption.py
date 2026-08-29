from cryptography.fernet import Fernet
import os


KEY_FILE = "secret.key"


def generate_key():
    key = Fernet.generate_key()

    with open(KEY_FILE, "wb") as file:
        file.write(key)

    print("Encryption key generated successfully.")


def load_key():
    if not os.path.exists(KEY_FILE):
        print("Encryption key not found.")
        print("Please generate a key first.")
        return None

    with open(KEY_FILE, "rb") as file:
        return file.read()


def encrypt_file(filename):
    key = load_key()

    if key is None:
        return

    if not os.path.exists(filename):
        print("File not found.")
        return

    try:
        with open(filename, "rb") as file:
            data = file.read()

        encrypted_data = Fernet(key).encrypt(data)

        encrypted_filename = filename + ".encrypted"

        with open(encrypted_filename, "wb") as file:
            file.write(encrypted_data)

        print(f"File encrypted successfully: {encrypted_filename}")

    except Exception as error:
        print("Error while encrypting file:", error)


def decrypt_file(filename):
    key = load_key()

    if key is None:
        return

    if not os.path.exists(filename):
        print("File not found.")
        return

    try:
        with open(filename, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = Fernet(key).decrypt(encrypted_data)

        if filename.endswith(".encrypted"):
            decrypted_filename = filename[:-10]
        else:
            decrypted_filename = filename + ".decrypted"

        with open(decrypted_filename, "wb") as file:
            file.write(decrypted_data)

        print(f"File decrypted successfully: {decrypted_filename}")

    except Exception:
        print("Error: Unable to decrypt the file.")
        print("Make sure the correct encryption key is being used.")


def main():
    print("===== File Encryption and Decryption =====")

    while True:
        print("\n1. Generate Encryption Key")
        print("2. Encrypt File")
        print("3. Decrypt File")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            generate_key()

        elif choice == "2":
            filename = input("Enter the file name to encrypt: ")
            encrypt_file(filename)

        elif choice == "3":
            filename = input("Enter the encrypted file name: ")
            decrypt_file(filename)

        elif choice == "4":
            print("Program terminated.")
            break

        else:
            print("Invalid choice. Please select between 1 and 4.")


if __name__ == "__main__":
    main()