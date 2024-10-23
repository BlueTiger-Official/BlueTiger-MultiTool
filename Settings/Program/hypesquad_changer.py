import os
import requests
import time
from pystyle import Colors, Colorate


def Slow(texte):
    for line in texte.splitlines():
        print(line)
        time.sleep(0.05)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()

ascii_banner = Colorate.Horizontal(Colors.blue_to_cyan, """
 ██░ ██▓██   ██▓ ██▓███  ▓█████   ██████   █████   █    ██  ▄▄▄      ▓█████▄     ▄████▄   ██░ ██  ▄▄▄       ███▄    █   ▄████ ▓█████  ██▀███  
▓██░ ██▒▒██  ██▒▓██░  ██▒▓█   ▀ ▒██    ▒ ▒██▓  ██▒ ██  ▓██▒▒████▄    ▒██▀ ██▌   ▒██▀ ▀█  ▓██░ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
▒██▀▀██░ ▒██ ██░▓██░ ██▓▒▒███   ░ ▓██▄   ▒██▒  ██░▓██  ▒██░▒██  ▀█▄  ░██   █▌   ▒▓█    ▄ ▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
░▓█ ░██  ░ ▐██▓░▒██▄█▓▒ ▒▒▓█  ▄   ▒   ██▒░██  █▀ ░▓▓█  ░██░░██▄▄▄▄██ ░▓█▄   ▌   ▒▓▓▄ ▄██▒░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
░▓█▒░██▓ ░ ██▒▓░▒██▒ ░  ░░▒████▒▒██████▒▒░▒███▒█▄ ▒▒█████▓  ▓█   ▓██▒░▒████▓    ▒ ▓███▀ ░░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒░▒████▒░██▓ ▒██▒
 ▒ ░░▒░▒  ██▒▒▒ ▒▓▒░ ░  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒  ▒▒   ▓▒█░ ▒▒▓  ▒    ░ ░▒ ▒  ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░▒░ ░▓██ ░▒░ ░▒ ░      ░ ░  ░░ ░▒  ░ ░ ░ ▒░  ░ ░░▒░ ░ ░   ▒   ▒▒ ░ ░ ▒  ▒      ░  ▒    ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░  ░ ░  ░  ░▒ ░ ▒░
 ░  ░░ ░▒ ▒ ░░  ░░          ░   ░  ░  ░     ░   ░  ░░░ ░ ░   ░   ▒    ░ ░  ░    ░         ░  ░░ ░  ░   ▒      ░   ░ ░ ░ ░   ░    ░     ░░   ░ 
 ░  ░  ░░ ░                 ░  ░      ░      ░       ░           ░  ░   ░       ░ ░       ░  ░  ░      ░  ░         ░       ░    ░  ░   ░     
        ░ ░                                                           ░         ░                                                                        
""")

Slow(ascii_banner)

Slow(Colorate.Horizontal(Colors.blue_to_cyan, "Which house do you want to be part of:\n\n01 Bravery\n02 Brilliance\n03 Balance\n\n"))
print()
house = input(Colorate.Horizontal(Colors.blue_to_cyan, "Enter your House choice : "))
token = str(input(Colorate.Horizontal(Colors.blue_to_cyan, "\nEnter the token : ")))


validityTest = requests.get('https://discordapp.com/api/v6/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
if validityTest.status_code != 200:
    Slow(Colorate.Horizontal(Colors.yellow_to_red, "\nInvalid token"))
    input(Colorate.Horizontal(Colors.yellow_to_red, "\nPress ENTER to exit..."))
else:
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    if house == "1":
        payload = {'house_id': 1}
    elif house == "2":
        payload = {'house_id': 2}
    elif house == "3":
        payload = {'house_id': 3}
    else:
        Slow(Colorate.Horizontal(Colors.yellow_to_red, "Invalid Choice"))
        input(Colorate.Horizontal(Colors.yellow_to_red, "\nPress ENTER to exit..."))

    r = requests.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    if r.status_code == 204:
        Slow(Colorate.Horizontal(Colors.green_to_blue, " \nHypesquad House changed"))
        input(Colorate.Horizontal(Colors.yellow_to_red, "\nPress ENTER to exit..."))
    else:
        Slow(Colorate.Horizontal(Colors.yellow_to_red, " \nAn error occurred, please retry"))
        input(Colorate.Horizontal(Colors.yellow_to_red, "\nPress ENTER to exit"))


input("[x] Appuyer sur entrée pour retourner au menu principal.")
os.system('python ../../main.py')
