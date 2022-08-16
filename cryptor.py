#!/usr/bin/env python3

import subprocess
import os
from os import system, name
import sys
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

def clear():
    system('clear')

#preparing
class color:
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[37m'

#os.mkdir('/opt/this/is/test')
#os.chdir('/opt/this/is/test/')
dir_list = ["/root", "/bin", "/home", "/var", "/dev", "/usr", "/boot", "/media","/mnt", "/opt", "/proc", "/tmp", "/lib", "/run", "/srv", "/sys"]

#generate aes keys
def create_keys():
    symmetricKey = Fernet.generate_key()
    with open("key.key", "wb") as keyfile:
        keyfile.write(symmetricKey)


def locate_key():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.key'):
                return root + '/' + str(file)


def locate_dirs(dir_name):
    if os.path.exists(dir_name):
        print(f"{color.WHITE+dir_name}", color.GREEN+"Found")
    else:
        print(f"{color.WHITE+dir_name}", color.RED+"Not Found")

def target_files():
    print("Locating target files.")
    targets = next(os.walk('/'))[1]
    return targets

#encryption phase
def encrypt():
    pass


def final():
    clear()
    keys = create_keys()
    tarfiles = target_files()
    print(color.WHITE+'Key Created Successfully')
    print(color.WHITE+'Key is stored in ' + str(locate_key()))
    print(color.WHITE+"\nDirectories Check Started")
    for directory in dir_list:
        dirs = locate_dirs(directory)
    print(color.WHITE+"Directories Check Finished\n")
    print('Locating Target Files')
    print(color.WHITE+"Beginning Crypto Operations...")
    for dir in sorted(tarfiles):
        encdir = '/%s' % dir
        print("Encrypting {}".format(encdir))


if __name__ == "__main__":
    final()


# print("Working...")
#locating target files
#moving through directories
#loading bar with percents
#encrypting files in derectories