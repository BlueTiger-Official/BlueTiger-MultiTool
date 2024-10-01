import os
import time
from colorama import Fore, Style
import fade


url_config = 'https://raw.githubusercontent.com/BlueTiger-Official/BlueTiger/Settings/config.py'
github_tool = 'https://github.com/BlueTiger-Official/BlueTiger'
DISCORD_LINK = ".gg/bluetiger"

version_tool = '1.0.0'
popup_version = "Version 1.0"

API_SEARCH = '' # SOON
API_AUTH_TOKEN = 'NKRZ-API-SEARCH-' # SOON

def get_username():
    return os.getlogin()

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def Slow(texte):
    delay = 0.03
    lignes = texte.split('\n')
    for ligne in lignes:
        print(ligne)
        time.sleep(delay)

def StartProgram(script_name):
    os.system(f'python {script_name}')

def Error(message):
    print(f"\033[1;31mError: {message}\033[0m")

def ErrorChoiceStart():
    print("\033[1;31mInvalid choice, please try again.\033[0m")

def get_banner(menu):
    banner = f"""                                                                                     
                    ▄▄▄▄    ██▓     █    ██ ▓█████    ▄▄▄█████▓ ██▓  ▄████ ▓█████  ██▀███  
                    ▓█████▄ ▓██▒     ██  ▓██▒▓█   ▀    ▓  ██▒ ▓▒▓██▒ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
                    ▒██▒ ▄██▒██░    ▓██  ▒██░▒███      ▒ ▓██░ ▒░▒██▒▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
                    ▒██░█▀  ▒██░    ▓▓█  ░██░▒▓█  ▄    ░ ▓██▓ ░ ░██░░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
                    ░▓█  ▀█▓░██████▒▒▒█████▓ ░▒████▒     ▒██▒ ░ ░██░░▒▓███▀▒░▒████▒░██▓ ▒██▒
                    ░▒▓███▀▒░ ▒░▓  ░░▒▓▒ ▒ ▒ ░░ ▒░ ░     ▒ ░░   ░▓   ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
                    ▒░▒   ░ ░ ░ ▒  ░░░▒░ ░ ░  ░ ░  ░       ░     ▒ ░  ░   ░  ░ ░  ░  ░▒ ░ ▒░
                     ░    ░   ░ ░    ░░░ ░ ░    ░        ░       ▒ ░░ ░   ░    ░     ░░   ░ 
                     ░          ░  ░   ░        ░  ░             ░        ░    ░  ░   ░     
                        ░                                                                                           

                                {github_tool} | {popup_version} 
                                            Discord : {DISCORD_LINK}
{menu}"""
    return banner

menu_path = "menu.txt"

def read_menu_state():
    if not os.path.exists(menu_path):
        return "1"
    
    with open(menu_path, "r") as file:
        menu = file.read().strip()
    
    return menu if menu in ["1", "2", "3","4","5"] else "1"

def write_menu_state(menu_number):
    with open(menu_path, "w") as file:
        file.write(menu_number)

def menu_exists():
    return os.path.exists(menu_path)

onion_link = [
    "http://onion1.onion",
    "http://onion2.onion",
    "http://onion3.onion",
    "http://onion4.onion"
]
