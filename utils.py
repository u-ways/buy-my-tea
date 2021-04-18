import getpass
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from cryptography.fernet import Fernet
from constant import TEN_SECONDS, DEFAULT_KEY_FILENAME, DEFAULT_PASSWORD_FILENAME


def generate_key(filename=DEFAULT_KEY_FILENAME):
    key = Fernet.generate_key()
    with open(filename, "wb") as secret_file:
        secret_file.write(key)


def encrypt_message(message, decrypt_key=DEFAULT_KEY_FILENAME):
    return Fernet(open(decrypt_key, "rb").read()) \
        .encrypt(message.encode())


def decrypt_message(message, decrypt_key=DEFAULT_KEY_FILENAME):
    return Fernet(open(decrypt_key, "rb").read()) \
        .decrypt(message.encode()).decode("utf-8")


def select(using, xpath, timeout=TEN_SECONDS):
    return WebDriverWait(using, timeout) \
        .until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))


# Just a small encryption and decryption script I recommend using
# if you're planing to store your own IG password as an env variable.
if __name__ == "__main__":
    pwd = getpass.getpass("Enter the password you want to encrypt:")
    generate_key()

    with open(DEFAULT_PASSWORD_FILENAME, "wb") as encrypted_password_file:
        encrypted_password_file.write(encrypt_message(pwd))

    print("encrypted password is at the root of this project: ./encrypted.password")
