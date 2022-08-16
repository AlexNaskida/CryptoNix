from os import system

from utils import create_symmetric_key
from config import starter_text, Color


def encrypt():
	print(starter_text, end="\n\n")

	# Symmetric key stuff
	key, key_path = create_symmetric_key()
	print(Color.WHITE + f'Key Created Successfully: {key}')
	print(Color.WHITE + 'Key is stored in ' + key_path)


if __name__ == "__main__":
	system('clear')
	encrypt()
