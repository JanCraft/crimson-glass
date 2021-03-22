import sys, os

VERSION = 'v0.1.1'
VERSION_NUMBER = 2

def clear():
    if 'win' in sys.platform:
        return os.system('cls')
    return os.system('clear')