import os
import requests
import subprocess
import time

def afficher_ascii_art():
    art = """
 █     █░ ▄▄▄       ██▓▄▄▄█████▓
▓█░ █ ░█░▒████▄    ▓██▒▓  ██▒ ▓▒
▒█░ █ ░█ ▒██  ▀█▄  ▒██▒▒ ▓██░ ▒░
░█░ █ ░█ ░██▄▄▄▄██ ░██░░ ▓██▓ ░ 
░░██▒██▓  ▓█   ▓██▒░██░  ▒██▒ ░ 
░ ▓░▒ ▒   ▒▒   ▓▒█░░▓    ▒ ░░   
  ▒ ░ ░    ▒   ▒▒ ░ ▒ ░    ░    
  ░   ░    ░   ▒    ▒ ░  ░      
    ░          ░  ░ ░           
         Wait it will download discord bot client                       
    """
    print(art)

def download_install_discord_bot_client(url, nom_fichier):
    afficher_ascii_art()
    response = requests.get(url)
    
    if response.status_code == 200:
        chemin_fichier = os.path.join(os.getcwd(), nom_fichier)
        with open(chemin_fichier, 'wb') as fichier:
            fichier.write(response.content)
        
        subprocess.run(chemin_fichier, shell=True)
        
        time.sleep(5)
        
        os.system(r'python ..\..\main.py')
    else:
        print("Erreur lors du téléchargement.")

url = 'https://github.com/aiko-chan-ai/DiscordBotClient/releases/latest/download/DiscordBotClient-win-x64.exe'
nom_fichier = 'DiscordBotClient-win-x64.exe'

download_install_discord_bot_client(url, nom_fichier)

import os    
input("[x] Appuyer sur entrée pour retourner au menu principal.")
os.system('python ../../main.py')
