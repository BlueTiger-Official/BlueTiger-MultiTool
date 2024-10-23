import subprocess
from colorama import Fore, Style, init
import os
import re
import time

os.system("cls")

def Slow(texte):
    for line in texte.splitlines():
        print(line)
        time.sleep(0.05)

interface = r"""
▓█████  ███▄ ▄███▓ ▄▄▄       ██▓ ██▓        ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀▓█████  ██▀███  
▓█   ▀ ▓██▒▀█▀ ██▒▒████▄    ▓██▒▓██▒       ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒███   ▓██    ▓██░▒██  ▀█▄  ▒██▒▒██░       ▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
▒▓█  ▄ ▒██    ▒██ ░██▄▄▄▄██ ░██░▒██░       ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
░▒████▒▒██▒   ░██▒ ▓█   ▓██▒░██░░██████▒   ▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
░░ ▒░ ░░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░▓  ░   ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ░ ░  ░░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░ ▒  ░     ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
   ░   ░      ░     ░   ▒    ▒ ░  ░ ░      ░         ░  ░░ ░   ░   ░        ░ ░░ ░    ░     ░░   ░ 
   ░  ░       ░         ░  ░ ░      ░  ░   ░ ░       ░  ░  ░   ░  ░░ ░      ░  ░      ░  ░   ░     
                                           ░                       ░                                                                                
"""
init(autoreset=True)
email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

def good_email(email):
    return re.match(email_regex, email) is not None

def cheker(email):
    result = subprocess.run(["holehe", email], capture_output=True, text=True)
    return result.stdout

def shores(email, data):
    lines = data.splitlines()
    used = [line for line in lines if "[+]"]
    
    if not used:
        return f"\n{Fore.CYAN}Résultats pour {email} :\n{Style.RESET_ALL}{Fore.RED}Aucun service utilisé\n{Style.RESET_ALL}"
    
    used = [line.replace("[+]", Fore.GREEN + "Utilisé pour " + Style.RESET_ALL) for line in used]
    
    return f"\n{Fore.CYAN}Résultats pour {email} :\n{Style.RESET_ALL}" + "\n".join(used)

def main():
    os.system("cls")
    Slow(interface)
    
    input_file_path = './Input/Email_uncheck.txt'
    try:
        with open(input_file_path, 'r') as file:
            emails = [line.strip() for line in file if good_email(line.strip())]
    except FileNotFoundError:
        Slow(Fore.RED + f"Erreur : Le fichier {input_file_path} n'a pas été trouvé." + Style.RESET_ALL)
        return
    
    if not emails:
        Slow(Fore.RED + "Erreur : Aucun email valide trouvé dans le fichier." + Style.RESET_ALL)
        return

    Slow(Fore.MAGENTA + "\nOn vérifie sa...\n" + Style.RESET_ALL)
    
    results = {}
    for email in emails:
        data = cheker(email)
        results[email] = shores(email, data)

    Slow(Fore.MAGENTA + "\nRésultats Total ->\n" + Style.RESET_ALL)
    
    output_file_path = './Output/Email_check.txt'
    with open(output_file_path, 'w') as output_file:
        for email, result in results.items():
            Slow(result)
            output_file.write(result + "\n")

    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')

if __name__ == "__main__":
    main()
