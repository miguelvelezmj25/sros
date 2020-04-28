# Specification: The test checks whether the system is configured securely. The test passes
# if crypt can decrypt the laser logs. If the test fails, the expected error
# is the AssertionError raised in this test. If another type of error besides "InvalidToken"
# is raised, then there is another error when attempting to decrypt the laser logs

from cryptography.fernet import InvalidToken
import crypt

try:
    crypt.main()
except InvalidToken:
    raise AssertionError("Could not decrypt the laser logs")

print("Test passed! Decrypted laser logs")