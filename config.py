# Terminal starter text
starter_text = """
 .o88b. d8888b. db    db d8888b. d888888b  .d88b.  d8b   db d888888b db    db 
d8P  Y8 88  `8D `8b  d8' 88  `8D `~~88~~' .8P  Y8. 888o  88   `88'   `8b  d8' 
8P      88oobY'  `8bd8'  88oodD'    88    88    88 88V8o 88    88     `8bd8'  
8b      88`8b      88    88~~~      88    88    88 88 V8o88    88     .dPYb.  
Y8b  d8 88 `88.    88    88         88    `8b  d8' 88  V888   .88.   .8P  Y8. 
 `Y88P' 88   YD    YP    88         YP     `Y88P'  VP   V8P Y888888P YP    YP 
  
                                                by Alex Naskidashvili
"""


# Terminal text colors
class Color:
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[37m'


DIRS = ['/root', '/home', '/var', '/dev', '/opt', '/srv', '/sys', '/bin', '/mnt', '/media', '/lost+found', '/lib',
        '/usr', '/sbin', '/proc', '/run', '/etc']

EXCLUDED_FILES = ['cryptonix.py', 'utils.py', 'config.py']

