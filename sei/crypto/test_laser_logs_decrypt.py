from cryptography.fernet import InvalidToken
import crypt
import logging

try:
    crypt.main()
    print("Test passed! Decrypted laser logs")
except InvalidToken as it:
    logging.exception("An exception was thrown!")