import fade
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config')))

from config import onion_link

def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)
    print()

def main():
    if isinstance(onion_link, list):
        onion_links_str = "\n".join(onion_link)
    else:
        onion_links_str = onion_link
    Slow(fade.water("""
 ▒█████   ███▄    █  ██▓ ▒█████   ███▄    █     ██▓     ██▓ ███▄    █  ██ ▄█▀  ██████ 
▒██▒  ██▒ ██ ▀█   █ ▓██▒▒██▒  ██▒ ██ ▀█   █    ▓██▒    ▓██▒ ██ ▀█   █  ██▄█▒ ▒██    ▒ 
▒██░  ██▒▓██  ▀█ ██▒▒██▒▒██░  ██▒▓██  ▀█ ██▒   ▒██░    ▒██▒▓██  ▀█ ██▒▓███▄░ ░ ▓██▄   
▒██   ██░▓██▒  ▐▌██▒░██░▒██   ██░▓██▒  ▐▌██▒   ▒██░    ░██░▓██▒  ▐▌██▒▓██ █▄   ▒   ██▒
░ ████▓▒░▒██░   ▓██░░██░░ ████▓▒░▒██░   ▓██░   ░██████▒░██░▒██░   ▓██░▒██▒ █▄▒██████▒▒
░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒    ░ ▒░▓  ░░▓  ░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░
  ░ ▒ ▒░ ░ ░░   ░ ▒░ ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░   ░ ░ ▒  ░ ▒ ░░ ░░   ░ ▒░░ ░▒ ▒░░ ░▒  ░ ░
░ ░ ░ ▒     ░   ░ ░  ▒ ░░ ░ ░ ▒     ░   ░ ░      ░ ░    ▒ ░   ░   ░ ░ ░ ░░ ░ ░  ░  ░  
    ░ ░           ░  ░      ░ ░           ░        ░  ░ ░           ░ ░  ░         ░  
                        Voici les liens Onion de Nkrz                                                                               
""" ))                                                                                     
                                                                                   

        
    print(fade.water(onion_links_str))
    
    while True:
        print(fade.water("\nAppuyez sur Entrée pour redémarrer ou 'q' pour quitter."))
        choix = input().strip().lower()
        if choix == 'q':
            break
        elif choix == '':
            input("[x] Appuyer sur entrée pour retourner au menu principal.")
            os.system('python ../../main.py')
        else:
            print(fade.water("Choix invalide. Appuyez sur Entrée pour redémarrer ou 'q' pour quitter."))

if __name__ == "__main__":
    main()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
