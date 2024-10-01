import socket
from datetime import datetime
import threading
import fade
import time
import sys
import os

def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)
    print()

banner = """                                                                            
 ██▓███   ▒█████   ██▀███  ▄▄▄█████▓    ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀
▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒   ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ 
▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░   ▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ 
▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░    ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ 
▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░    ▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄
▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░      ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒
░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░         ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░
░░       ░ ░ ░ ▒    ░░   ░   ░         ░         ░  ░░ ░   ░   ░        ░ ░░ ░ 
             ░ ░     ░                 ░ ░       ░  ░  ░   ░  ░░ ░      ░  ░   
                                       ░                       ░                                                                                             
"""

faded_banner = fade.water(banner)
Slow(faded_banner)
def get_target():
    hostname = input(fade.water("Enter your target hostname (or IP address) : "))
    target = socket.gethostbyname(hostname)
    Slow(f'Scan Target  > {target}')
    return target

def get_port_list():
    Slow(f'Ports Range  > [1 – 1024]')
    return range(1, 1024)

def scan_port(target, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        test = s.connect_ex((target, port))
        if test == 0:
            Slow(f'Port {port} is [open]')

def port_scanner():
    try:
        target = get_target()
        port_list = get_port_list()
        thread_list = list()
        start_time = datetime.now()

        for port in port_list:
            scan = threading.Thread(target=scan_port, args=(target, port))
            thread_list.append(scan)
            scan.daemon = True
            scan.start()

        for scan in thread_list:
            scan.join()
    except:
        Slow("Something went wrong !")
    else:
        end_time = datetime.now()
        Slow("Scanning completed in " + str(end_time - start_time))
        input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')

if __name__ == '__main__':
    port_scanner()
