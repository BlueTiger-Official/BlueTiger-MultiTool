import random
import string
import requests
import sys
import os
from os import system as cmd
from time import sleep as wait
import fade

sys.stdout.reconfigure(encoding='utf-8')

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)
    print()

class color:
    RED = fade.water
    GREEN = fade.water
    WHITE = fade.water
    RESET = fade.water

amount = 0

def make_code(length=19):
    characters = string.ascii_uppercase + string.digits
    nitro_code = ''.join(random.choice(characters) for _ in range(length))
    return nitro_code

def check_code(code):
    valid = requests.get(f'https://discord.com/api/v9/entitlements/gift-codes/{code}')
    return valid.status_code == 200

title = '''
 ███▄    █  ██▓▄▄▄█████▓ ██▀███   ▒█████  
 ██ ▀█   █ ▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒
▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒
▓██▒  ▐▌██▒░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░
▒██░   ▓██░░██░  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░
░ ▒░   ▒ ▒ ░▓    ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░ 
░ ░░   ░ ▒░ ▒ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░ 
   ░   ░ ░  ▒ ░  ░        ░░   ░ ░ ░ ░ ▒  
         ░  ░              ░         ░ ░  
                                          
        Force a toi pour en avoir un 
'''

fadetitle = fade.water(title)

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
output_dir = os.path.join(parent_dir, 'Output', 'nitro-codes')

os.makedirs(output_dir, exist_ok=True)

while not amount >= 1:
    clear()
    Slow(fadetitle)
    amount = input(fade.water('[?] Entrez le nombre de codes à générer (Conseil, mettez minimum 1000) : '))

    try:
        amount = int(amount)
        if amount <= 0:
            Slow(fade.water('[!] Erreur : Veuillez entrer un nombre au dessus de 0'))
            input()
            sys.exit()
    except ValueError:
        Slow(fade.water('[!] Erreur: Veuillez entrer un nombre valide'))
        input()
        sys.exit()

print('\n')

output_file = os.path.join(output_dir, 'nitro-codes.txt')

with open(output_file, 'w') as file:
    for i in range(amount):
        code = make_code()
        valid = check_code(code)
        if valid:
            print(fade.water(f'[!] Code Nitro valide trouvé : {code} lors de la tentative [{i + 1}]'))
            file.write(f'{code} - VALIDE\n')
        else:
            print(fade.water(f'[!] Code Nitro invalide trouvé : {code} lors de la tentative [{i + 1}]'))
            file.write(f'{code} - INVALIDE\n')

Slow(fade.water('[!] Fin de la génération '))

input("[x] Appuyer sur entrée pour retourner au menu principal.")
os.system('python ../../main.py')
