import requests
import time
import os
import sys
import fade

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def set_title(title):
    if os.name == 'nt':
        os.system(f'title {title}')
    else:
        sys.stdout.write(f'\33]0;{title}\a')
        sys.stdout.flush()

def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)
    print()

def main():
    clear()
    set_title("Nkrz Multi-Tool Token Checker")
    Slow(ascii_banner)
    file_path = input(fade.water("Enter the file path : "))
    
    if not file_path:
        Slow(fade.water("! No file path provided."))
        return

    donetokenlist = load_tokens(file_path)
    if not donetokenlist:
        Slow(fade.water("! No tokens loaded."))
        return

    check_and_display_results(donetokenlist)

ascii_banner = fade.water("""
▄▄▄█████▓ ▒█████   ██ ▄█▀▓█████  ███▄    █     ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀▓█████  ██▀███  
▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒ ▓█   ▀  ██ ▀█   █    ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒ ▓██░ ▒░▒██░  ██▒▓███▄░ ▒███   ▓██  ▀█ ██▒   ▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
░ ▓██▓ ░ ▒██   ██░▓██ █▄ ▒▓█  ▄ ▓██▒  ▐▌██▒   ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
  ▒██▒ ░ ░ ████▓▒░▒██▒ █▄░▒████▒▒██░   ▓██░   ▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
  ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒░   ▒ ▒    ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
    ░      ░ ▒ ▒░ ░ ░▒ ▒░ ░ ░  ░░ ░░   ░ ▒░     ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
  ░      ░ ░ ░ ▒  ░ ░░ ░    ░      ░   ░ ░    ░         ░  ░░ ░   ░   ░        ░ ░░ ░    ░     ░░   ░ 
             ░ ░  ░  ░      ░  ░         ░    ░ ░       ░  ░  ░   ░  ░░ ░      ░  ░      ░  ░   ░     
                                              ░                       ░                                                                                                                                                             
""")

def load_tokens(file_path):
    loaded_amount = 0
    donetokenlist = []
    try:
        with open(file_path, "r") as checklist:
            tokenlist = checklist.readlines()
        for token in tokenlist:
            donetokenlist.append(token.strip())
            loaded_amount += 1
        Slow(fade.water(f"\n+ {loaded_amount} Tokens Loaded"))
        input(fade.water("Press ENTER to start"))
        return donetokenlist
    except FileNotFoundError:
        Slow(fade.water("! File not found"))
        input(fade.water("Press ENTER to exit"))
        return []

def check_and_display_results(donetokenlist):
    clear()
    valid_tokens = []
    invalid_tokens = []
    invite_code = "HhQwbnzda2"

    for token in donetokenlist:
        while True:
            try:
                r1 = requests.post('https://discord.com/api/v9/auth/login', headers={"Authorization": token})
                if r1.status_code != 200:
                    if r1.status_code == 429:
                        Slow(fade.water('! Rate limited...'))
                        time.sleep(5)
                        continue
                    elif r1.status_code == 401:
                        Slow(fade.water(f"! Invalid: {token}"))
                        invalid_tokens.append(token)
                        break
                    else:
                        Slow(fade.water(f"! Unknown error: {token} (Status Code: {r1.status_code})"))
                        invalid_tokens.append(token)
                        break
                else:
                    break
            
            except requests.exceptions.RequestException as e:
                Slow(fade.water(f"! Request error: {e}"))
                invalid_tokens.append(token)
                break
        
        if r1.status_code == 200:
            while True:
                try:
                    r = requests.get('https://discord.com/api/v9/users/@me', headers={"Authorization": token})
                    if r.status_code != 200:
                        if r.status_code == 429:
                            Slow(fade.water('! Rate limited...'))
                            time.sleep(5)
                            continue
                        elif r.status_code == 401:
                            Slow(fade.water(f"! Verification required: {token}"))
                            invalid_tokens.append(token)
                            break
                        else:
                            Slow(fade.water(f"! Unknown error: {token} (Status Code: {r.status_code})"))
                            invalid_tokens.append(token)
                            break
                    else:
                        Slow(fade.water(f"! Valid: {token}"))
                        valid_tokens.append(token)
                        break
                
                except requests.exceptions.RequestException as e:
                    Slow(fade.water(f"! Request error: {e}"))
                    invalid_tokens.append(token)
                    break

    Slow(fade.water(f"\n\n+ Results:\n"))
    
    if valid_tokens:
        Slow(fade.water("Valid tokens:"))
        for token in valid_tokens:
            Slow(fade.water(f"  + {token}"))
    
    if invalid_tokens:
        Slow(fade.water("\nInvalid tokens:"))
        for token in invalid_tokens:
            Slow(fade.water(f"  ! {token}"))

    input(fade.water("\n\n Press ENTER to exit"))
    main()

if __name__ == "__main__":
    main()
    
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
