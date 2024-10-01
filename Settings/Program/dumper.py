import os
import time
import requests
import json
import re
import uuid
from fake_useragent import UserAgent
from colorama import init, Fore, Style
import fade

init(autoreset=True)

def clean_filename(hostname):
    return re.sub(r'[^a-zA-Z0-9_\-]', '', hostname)

def check_if_player_exists(filename, player_data, added_players):
    if not os.path.exists(filename):
        return False

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        try:
            existing_player = json.loads(line)
        except json.JSONDecodeError:
            continue

        if existing_player.get('fivem') == player_data.get('fivem'):
            fields_to_check = ['steam', 'name', 'live', 'xbl', 'license', 'license2', 'name']
            fields_match = all(existing_player.get(field) == player_data.get(field) for field in fields_to_check)

            if fields_match:
                return True

    if player_data['identifiers'] in added_players:
        return True

    return False

def get_server_info(server_id, proxy, added_players):
    url = f'https://servers-frontend.fivem.net/api/servers/single/{server_id}'
    user_agent = UserAgent()
    headers = {
        'User-Agent': user_agent.random,
        'method': 'GET'
    }

    try:
        response = requests.get(url, headers=headers, proxies=proxy)

        if response.status_code == 200:
            server_data = response.json()
            hostname = clean_filename(server_data.get('Data', {}).get('hostname', str(uuid.uuid4()))[:100])

            project_name = server_data.get('Data', {}).get('vars', {}).get('sv_projectName')
            if project_name and len(project_name) >= 10:
                hostname = clean_filename(project_name[:100])

            output_dir = os.path.join('..', 'Output')
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            dump_dir = os.path.join(output_dir, 'FivemDump')
            if not os.path.exists(dump_dir):
                os.makedirs(dump_dir)

            filename = os.path.join(dump_dir, f'{hostname}.txt')
            players_added_count = 0

            for player in server_data['Data'].get('players', []):
                if not check_if_player_exists(filename, player, added_players):
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(json.dumps(player, ensure_ascii=False))
                        file.write('\n')

                    print(Fore.GREEN + f'[NEW]' + Style.RESET_ALL + f' {player["name"]} a été ajouté !')
                    added_players.append(player['identifiers'])
                    players_added_count += 1

            print(Fore.CYAN + f'[Nkrz Multi-Tool]' + Style.RESET_ALL + f' Nombre de joueurs ajoutés dans {filename}: {players_added_count}')
            print(Fore.CYAN + '[Nkrz Multi-Tool]' + Style.RESET_ALL + f' Nombre total de joueurs ajoutés : {len(added_players)}\n')

        else:
            print(Fore.RED + f'\n[ERROR]' + Style.RESET_ALL + f" Message d'erreur ({server_id}: {response.status_code})\n")

    except requests.RequestException as e:
        print(Fore.RED + f'\n[ERROR]' + Style.RESET_ALL + f" Erreur de requête ({server_id}): {str(e)}\n")

def process_servers(server_ids, proxies, added_players):
    for server_id, proxy in zip(server_ids, proxies):
        get_server_info(server_id, proxy, added_players)
        time.sleep(0.5)

def wait_for_enter():
    input("Appuyez sur Entrée pour démarrer le processus de dump... ajouter des cfx.id dans le fichier Input/serveur.txt")

def main():
    wait_for_enter()

    input_dir = os.path.join('..', 'Input')
    with open(os.path.join(input_dir, 'serveur.txt'), 'r') as server_file:
        french_server_ids = [line.strip() for line in server_file.readlines()]

    with open(os.path.join(input_dir, 'proxy.txt'), 'r') as proxy_file:
        proxy_list = [{'http': f'socks5://{proxy.strip()}'} for proxy in proxy_file]

    added_players = []

    while True:
        half_length = len(french_server_ids) // 2
        first_half = french_server_ids[:half_length]
        second_half = french_server_ids[half_length:]

        process_servers(first_half, proxy_list, added_players)
        process_servers(second_half, proxy_list, added_players)

        print(Fore.MAGENTA + "\n[TIME]" + Style.RESET_ALL + " dump fini veuillez patienter pour le prochain (10sec) ...\n")
        time.sleep(10)

def startup():
    os.system("cls" if os.name == "nt" else "clear")
    banner = '''
▓█████▄  █    ██  ███▄ ▄███▓ ██▓███  ▓█████  ██▀███      ▄▄▄▄ ▓██   ██▓    ███▄    █  ██ ▄█▀ ██▀███  ▒███████▒     ▓█████▄  ██▓     ██▓    
▒██▀ ██▌ ██  ▓██▒▓██▒▀█▀ ██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒   ▓█████▄▒██  ██▒    ██ ▀█   █  ██▄█▒ ▓██ ▒ ██▒▒ ▒ ▒ ▄▀░     ▒██▀ ██▌▓██▒    ▓██▒    
░██   █▌▓██  ▒██░▓██    ▓██░▓██░ ██▓▒▒███   ▓██ ░▄█ ▒   ▒██▒ ▄██▒██ ██░   ▓██  ▀█ ██▒▓███▄░ ▓██ ░▄█ ▒░ ▒ ▄▀▒░      ░██   █▌▒██░    ▒██░    
░▓█▄   ▌▓▓█  ░██░▒██    ▒██ ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄     ▒██░█▀  ░ ▐██▓░   ▒██░   ▓██░▒██▒ █▄░██▓ ▒██▒▒███████▒ ██▓ ░▒████▓ ░██████▒░██████▒
 ▒▒▓  ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░▒▓▒░ ░  ░░▒████▒░██▓ ▒██▒   ░▓█  ▀█▓░ ██▒▓░   ▒██░   ▒ ▒ ▒ ▒▒ ▓▒░ ▒▓ ░▒▓░░▒▒ ▓░▒░▒ ▒▓▒  ▒▒▓  ▒ ░ ▒░▓  ░░ ▒░▓  ░
 ░ ▒  ▒ ░░▒░ ░ ░ ░  ░      ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░   ▒░▒   ░▓██ ░▒░    ░ ▒░   ░ ▒░░ ░▒ ▒░  ░▒ ░ ▒░░░▒ ▒ ░ ▒ ░▒   ░ ▒  ▒ ░ ░ ▒  ░░ ░ ▒  ░
 ░ ░  ░  ░░░ ░ ░ ░      ░   ░░          ░     ░░   ░     ░    ░▒ ▒ ░░        ░   ░ ░ ░ ░░ ░   ░░   ░ ░ ░ ░ ░ ░ ░    ░ ░  ░   ░ ░     ░ ░   
   ░       ░            ░               ░  ░   ░         ░     ░ ░                 ░ ░  ░      ░       ░ ░      ░     ░        ░  ░    ░  ░
 ░                                                            ░░ ░                                   ░          ░   ░                      

                                                     ╔══════════════════╗
                                                     ║ Nkrz Dumper      ║
                                                     ║ Made By Nkrz.dll ║
                                                     ╚══════════════════╝                                                                                                                                                                                                                                                                                                                                                                                                                      
'''
    faded_text = fade.purplepink(banner)
    print(faded_text)

    wait_for_enter()
    main()

startup()
import os    
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
