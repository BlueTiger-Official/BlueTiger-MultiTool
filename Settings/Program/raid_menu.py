import os
import sys
import asyncio
import fade
import time
from utils import tokenbot, webhook, tokenuser, tokennuker, groupspammer

def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)
    print()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_ascii_art():
    art = """
 ██▀███   ▄▄▄       ██▓▓█████▄ 
▓██ ▒ ██▒▒████▄    ▓██▒▒██▀ ██▌
▓██ ░▄█ ▒▒██  ▀█▄  ▒██▒░██   █▌
▒██▀▀█▄  ░██▄▄▄▄██ ░██░░▓█▄   ▌
░██▓ ▒██▒ ▓█   ▓██▒░██░░▒████▓ 
░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▓   ▒▒▓  ▒ 
  ░▒ ░ ▒░  ▒   ▒▒ ░ ▒ ░ ░ ▒  ▒ 
  ░░   ░   ░   ▒    ▒ ░ ░ ░  ░ 
   ░           ░  ░ ░     ░    
                        ░      
                                                                        
[01] > Token Bot       
[02] > Webhook URL                   
[03] > Token User              
[04] > Token Nuker
[05] > Group Spammer
    """
    colored_art = fade.water(art)
    Slow(colored_art)

def main():
    while True:
        clear()
        print_ascii_art()
        choice = input(fade.water("Choose Options : "))

        if choice == "1":
            tokenbot.token_bot()
        elif choice == "2":
            asyncio.run(webhook.main()) 
        elif choice == "3":
            asyncio.run(tokenuser.main())
        elif choice == "4":
            tokennuker.Token_nuker()
        elif choice == "5":
            groupspammer.main() 
        else:
            Slow(fade.water("Invalid choice. Please choose 1, 2, 3, 4 or 5"))
            sys.exit(1)

if __name__ == "__main__":
    main()
        input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
