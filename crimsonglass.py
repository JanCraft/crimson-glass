import sys, os, time
from pathlib import Path

import src.system as system
import src.config as cfg

import colorama
from colorama import Fore, Back, Style

system.cwd = str(Path.home())
cfg.clear()
print(Fore.RED + "CrimsonGlass vOS " + Fore.GREEN + "(" + cfg.VERSION + ")")

while True:
    try:
        inp = input(Fore.BLUE + Style.BRIGHT + system.cwd + Style.RESET_ALL + Fore.RESET + "$ ")
        if not system.process(inp):
            break
    except KeyboardInterrupt:
        print()