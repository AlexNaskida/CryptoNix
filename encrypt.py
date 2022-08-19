#!/usr/bin/env python3
from os import system

from utils import create_symmetric_key, encrypt_target_files
from config import starter_text, Color


def encrypt() -> None:
	print(starter_text, end="\n\n")

	# Symmetric key stuff
	symmetric_key, symmetric_key_path = create_symmetric_key()
	print(Color.WHITE + f'Key Created Successfully: {symmetric_key}')
	print(Color.WHITE + 'Key is stored in ' + symmetric_key_path)

	# Encrypt files
	encrypt_target_files(symmetric_key)


if __name__ == "__main__":
	system('clear')
	encrypt()
