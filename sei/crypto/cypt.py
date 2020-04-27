from cryptography.fernet import Fernet
import os


def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_public_key():
    """
    Loads the key from the current directory named `public.key`
    """
    return open("public.key", "rb").read()


def load_secret_key():
    """
    Loads the key from the current directory named `secret.key`
    """
    return open("secret.key", "rb").read()


def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)


def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Simple File Encryptor Script")
    parser.add_argument("-e", "--encrypt", action="store_true",
                        help="Whether to encrypt the file, only -e or -d can be specified.")
    parser.add_argument("-d", "--decrypt", action="store_true",
                        help="Whether to decrypt the file, only -e or -d can be specified.")

    args = parser.parse_args()

    file = "laser_logs.txt"

    if args.encrypt:
        if os.getenv('CRYPT_SECURITY_ENABLE') == 'true':
            key = load_secret_key()
        else:
            key = load_public_key()

        encrypt(file, key)
    elif args.decrypt:
        if os.getenv('CRYPT_SECURITY_ENABLE') == 'true':
            key = load_secret_key()
        else:
            key = load_public_key()

        decrypt(file, key)


if __name__ == "__main__":
    main()
