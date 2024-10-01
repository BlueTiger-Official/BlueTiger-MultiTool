import requests
import time
import threading
import fade
import subprocess
import os

def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)
    print()

def get_headers(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
    }
    return headers

def new_title(title):
    print(f"{fade.water(title)}")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    ascii_art = """
  ██████ ▄▄▄█████▓ ▄▄▄     ▄▄▄█████▓ █    ██   ██████     ██▀███   ▒█████  ▄▄▄█████▓ ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
▒██    ▒ ▓  ██▒ ▓▒▒████▄   ▓  ██▒ ▓▒ ██  ▓██▒▒██    ▒    ▓██ ▒ ██▒▒██▒  ██▒▓  ██▒ ▓▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄ ▒ ▓██░ ▒░▓██  ▒██░░ ▓██▄      ▓██ ░▄█ ▒▒██░  ██▒▒ ▓██░ ▒░▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
  ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██░ ▓██▓ ░ ▓▓█  ░██░  ▒   ██▒   ▒██▀▀█▄  ▒██   ██░░ ▓██▓ ░ ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒ ▒██▒ ░ ▒▒█████▓ ▒██████▒▒   ░██▓ ▒██▒░ ████▓▒░  ▒██▒ ░  ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░ ▒ ░░   ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░   ▒ ░░    ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
░ ░▒  ░ ░    ░      ▒   ▒▒ ░   ░    ░░▒░ ░ ░ ░ ░▒  ░ ░     ░▒ ░ ▒░  ░ ▒ ▒░     ░      ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
░  ░  ░    ░        ░   ▒    ░       ░░░ ░ ░ ░  ░  ░       ░░   ░ ░ ░ ░ ▒    ░        ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
      ░                 ░  ░           ░           ░        ░         ░ ░                 ░  ░            ░ ░     ░     
                                                                                                                                                                                                                                                                                                 
    """
    colored_ascii = fade.water(ascii_art)
    print(colored_ascii)

def read_status_texts():
    Slow(fade.water('Entrer le statut que vous voulez mettre et entrer FIN quand vous avez fini :'))
    status_texts = []
    index = 1
    
    while True:
        line = input(fade.water(f'Status {index}): '))
        
        if line.upper() == "FIN":
            break
        
        status_texts.append(line)
        index += 1
    
    return status_texts

def change_status(token, text):
    clear()
    headers = get_headers(token)
    setting = {
        'custom_status': {
            'text': text,
        },
    }
    r = requests.patch("https://discord.com/api/v6/users/@me/settings", headers=headers, json=setting)
    if r.status_code == 200:
        Slow(fade.water(f'token={token[:20]}... [SUCCESS]'))
    else:
        Slow(fade.water(f'token={token[:20]}... [ERROR] ({r.status_code})'))

def status_changer():
    clear()
    banner()
    
    token = input(fade.water('Entrez le token: '))
    
    status_texts = read_status_texts()
    
    while True:
        try:
            time_frequency = int(input(fade.water('Temps entre chaque changement de statut (en secondes) : '))
            break
        except ValueError:
            Slow(fade.water('Veuillez entrer un nombre entier pour le temps.'))
    
    while True:
        try:
            for text in status_texts:
                thread = threading.Thread(target=change_status, args=(token, text))
                thread.start()
                thread.join()
                time.sleep(time_frequency)
        except KeyboardInterrupt:
            Slow(fade.water('Interruption du changement de statut.'))

if __name__ == "__main__":
    status_changer()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
