import sys, os

cwd = '/'

def process(line):
    line = line.strip()
    if line.startswith("exit"):
        if len(line[5:]) > 0:
            print(line[5:])
        return False
    elif line.startswith("subos"):
        os.system(line[6:])
    return True