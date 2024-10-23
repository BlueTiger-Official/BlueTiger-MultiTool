import requests
import time
import os
from colorama import Fore

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def Slow(texte):
    for line in texte.splitlines():
        print(line)
        time.sleep(0.05)


ascii_banner = f"""{Fore.RED}

 ██▓     ▒█████    ▄████  ██▓ ███▄    █    ▄▄▄█████▓ ▒█████   ██ ▄█▀▓█████  ███▄    █ 
▓██▒    ▒██▒  ██▒ ██▒ ▀█▒▓██▒ ██ ▀█   █    ▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒ ▓█   ▀  ██ ▀█   █ 
▒██░    ▒██░  ██▒▒██░▄▄▄░▒██▒▓██  ▀█ ██▒   ▒ ▓██░ ▒░▒██░  ██▒▓███▄░ ▒███   ▓██  ▀█ ██▒
▒██░    ▒██   ██░░▓█  ██▓░██░▓██▒  ▐▌██▒   ░ ▓██▓ ░ ▒██   ██░▓██ █▄ ▒▓█  ▄ ▓██▒  ▐▌██▒
░██████▒░ ████▓▒░░▒▓███▀▒░██░▒██░   ▓██░     ▒██▒ ░ ░ ████▓▒░▒██▒ █▄░▒████▒▒██░   ▓██░
░ ▒░▓  ░░ ▒░▒░▒░  ░▒   ▒ ░▓  ░ ▒░   ▒ ▒      ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒░   ▒ ▒ 
░ ░ ▒  ░  ░ ▒ ▒░   ░   ░  ▒ ░░ ░░   ░ ▒░       ░      ░ ▒ ▒░ ░ ░▒ ▒░ ░ ░  ░░ ░░   ░ ▒░
  ░ ░   ░ ░ ░ ▒  ░ ░   ░  ▒ ░   ░   ░ ░      ░      ░ ░ ░ ▒  ░ ░░ ░    ░      ░   ░ ░ 
    ░  ░    ░ ░        ░  ░           ░                 ░ ░  ░  ░      ░  ░         ░ 
                                                                                          
                                                              
"""

Slow(ascii_banner)

def autologin():
    from selenium import webdriver
    clear()
    Slow("Enter the token of the account you want to connect to")
    entertoken = input("Token: ")
    
    validityTest = requests.get('https://discordapp.com/api/v6/users/@me', headers={'Authorization': entertoken, 'Content-Type': 'application/json'})
    if validityTest.status_code != 200:
        Slow("\nInvalid token")
        input("Press ENTER to exit")
        os.system('python ../../main.py')

    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get('https://discord.com/login')
        
        js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'

        time.sleep(3)
        driver.execute_script(js + f'login("{entertoken}")')
        time.sleep(10)

        if driver.current_url == 'https://discord.com/login':
            clear()
            Slow("Connection Failed")
            driver.close()
        else:
            clear()
            Slow("Connection Established")
        
        input("Press ENTER to exit")

    except Exception as e:
        Slow(f"A problem occurred: {e}")
        time.sleep(2)
        clear()

input(Fore.BLUE + "[x] Appuyer sur entrée pour retourner au menu principal.")
os.system('python ../../main.py')

autologin()

