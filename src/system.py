import sys, os, pathlib, psutil, math
import src.config as cfg
import colorama
from colorama import Fore, Back, Style

cwd = '/'

def togb(b):
    b /= 1024 ** 3
    return str(round(b, ndigits=2)) + 'GB'

def process(line):
    global cwd
    line = line.strip()
    if line.startswith("exit"):
        if len(line[5:]) > 0:
            print(line[5:])
        return False
    elif line.startswith("subos"):
        os.system(line[6:])
    elif line.startswith('pwd'):
        print(cwd)
    elif line.startswith('cd'):
        p = os.path.join(cwd, line[3:])
        if os.path.exists(p):
            cwd = str(p)
        else:
            print(line[3:] + ": no such directory")
    elif line.startswith('ls'):
        os.system(line + ' ' + cwd)
    elif line.startswith('rm'):
        p = os.path.join(cwd, line[3:])
        try:
            os.remove(p)
        except Exception as e:
            print(e)
    elif line.startswith('rmdir'):
        p = os.path.join(cwd, line[3:])
        try:
            os.rmdir(p)
        except Exception as e:
            print(e)
    elif line.startswith('mkdir'):
        p = os.path.join(cwd, line[3:])
        try:
            os.mkdir(p)
        except Exception as e:
            print(e)
    elif line.startswith('cp'):
        p1 = os.path.join(cwd, line.split(' ')[1])
        p2 = os.path.join(cwd, line.split(' ')[2])
        try:
            with open(str(p1), 'rb') as f1:
                with open(str(p2), 'wb') as f2:
                    f2.write(f1.read())
        except Exception as e:
            print(e)
    elif line.startswith('mv'):
        p1 = os.path.join(cwd, line.split(' ')[1])
        p2 = os.path.join(cwd, line.split(' ')[2])
        try:
            os.rename(p1, p2)
        except Exception as e:
            print(e)
    elif line.startswith('touch'):
        sp = line.split(' ')[1:]
        for pd in sp:
            p = os.path.join(cwd, pd)
            f = open(str(p), 'w')
            f.close()
    elif line.startswith('cat'):
        sp = line.split(' ')[1:]
        for pd in sp:
            p = os.path.join(cwd, pd)
            f = open(str(p), 'r')
            print(f.read())
            f.close()
    elif line.startswith('clear'):
        cfg.clear()
    elif line.startswith('echo'):
        print(line[5:])
    elif line.startswith('shutdown'):
        if 'confirm' in line:
            os.system('systemctl poweroff')
        else:
            print('Use "shutdown confirm" if you really want to shutdown the machine')
    elif line.startswith('reboot'):
        if 'confirm' in line:
            os.system('systemctl reboot')
        else:
            print('Use "reboot confirm" if you really want to reboot the machine')
    elif line.startswith('sysinfo'):
        print("CrimsonGlass vOS (" + cfg.VERSION + ")")
        print("Sub. OS:", sys.platform.capitalize())
        print("Python Runtime:", '.'.join([str(sys.version_info.major), str(sys.version_info.minor), str(sys.version_info.micro)]))
        print("CPU Count:", os.cpu_count())
        print("RAM Usage:", togb(psutil.virtual_memory().used) + '/' + togb(psutil.virtual_memory().total))
    else:
        print(line.split(' ')[0] + ": not found")
    return True