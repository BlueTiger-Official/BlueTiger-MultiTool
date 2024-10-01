import os, socket
import fade
import time

def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)
    print()

hostname = socket.gethostname()
host = socket.gethostbyname(hostname)

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def scan_ip(ip): 
    Slow(fade.water('[*] Scanning...\n'))
    for port in range(65535):   
        serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv.settimeout(1)
        try:
            serv.connect((ip, port))
            Slow(fade.water(f'[OPEN]: Port {port} -->  [{ip}:{port}]'))
        except:
            pass
        finally:
            serv.close() 

def main():
    while True:
        clear()
        title = f'''
  ██████  ▄████▄   ▄▄▄       ███▄    █  ███▄    █ ▓█████  █    ██  ██▀███  
▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █  ██ ▀█   █ ▓█   ▀  ██  ▓██▒▓██ ▒ ██▒
░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▓██  ▒██░▓██ ░▄█ ▒
  ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▓▓█  ░██░▒██▀▀█▄  
▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░░▒████▒▒▒█████▓ ░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░
░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░░░▒░ ░ ░   ░▒ ░ ▒░
░  ░  ░  ░          ░   ▒      ░   ░ ░    ░   ░ ░    ░    ░░░ ░ ░   ░░   ░ 
      ░  ░ ░            ░  ░         ░          ░    ░  ░   ░        ░     
         ░                                                                 
                    Your public ip is :  [{host}]
'''
        Slow(fade.water(title))

        ip = input(fade.water('[*] Enter the IP to scan: '))
        scan_ip(ip)

        choice = input(fade.water('[*] Press ENTER to return the menu or type "exit" to quit: '))
        if choice.lower() == "exit":
            break

if __name__ == "__main__":
    main()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
