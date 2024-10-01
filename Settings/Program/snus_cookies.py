import subprocess
import sys
import time
import os

def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)
    print()

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import selenium
except ImportError:
    install("selenium")

try: 
    import fade
except ImportError:
    install("fade")

try:
    import webdriver_manager
except ImportError:
    install("webdriver_manager")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_experimental_option("detach", True)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    return driver

def add_cookies(driver):
    cookies = [
        {'name': 'lg', 'value': 'b27283a87bd840cd1d6164a2c641ec1512c20208649604ed8985eddd2c5cdc0d', 'domain': 'snusbase.com'},
        {'name': 'rm', 'value': 'dWtwUlZEaEJ6bnhTckZpQ3VRWkhqdz09%3A%3Atmpd1DMiIIK4otOCcpCuWg%3D%3D', 'domain': 'snusbase.com'},
        {'name': 'a', 'value': '9p1l9soconm2t71l0idltkqf9o', 'domain': 'snusbase.com'},
    ]

    for cookie in cookies:
        driver.add_cookie(cookie)    

def main():
    print(f"\033]0;Nkrz cookies Snubase\007")
    Slow(fade.water('''

  ██████  ███▄    █  █    ██   ██████  ▄▄▄▄    ▄▄▄        ██████ ▓█████    ▄▄▄█████▓ ▒█████   ▒█████   ██▓        ███▄    █  ██ ▄█▀ ██▀███  ▒███████▒     ▓█████▄  ██▓     ██▓    
▒██    ▒  ██ ▀█   █  ██  ▓██▒▒██    ▒ ▓█████▄ ▒████▄    ▒██    ▒ ▓█   ▀    ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒        ██ ▀█   █  ██▄█▒ ▓██ ▒ ██▒▒ ▒ ▒ ▄▀░     ▒██▀ ██▌▓██▒    ▓██▒    
░ ▓██▄   ▓██  ▀█ ██▒▓██  ▒██░░ ▓██▄   ▒██▒ ▄██▒██  ▀█▄  ░ ▓██▄   ▒███      ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░       ▓██  ▀█ ██▒▓███▄░ ▓██ ░▄█ ▒░ ▒ ▄▀▒░      ░██   █▌▒██░    ▒██░    
  ▒   ██▒▓██▒  ▐▌██▒▓▓█  ░██░  ▒   ██▒▒██░█▀  ░██▄▄▄▄██   ▒   ██▒▒▓█  ▄    ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░       ▓██▒  ▐▌██▒▓██ █▄ ▒██▀▀█▄    ▄▀▒   ░     ░▓█▄   ▌▒██░    ▒██░    
▒██████▒▒▒██░   ▓██░▒▒█████▓ ▒██████▒▒░▓█  ▀█▓ ▓█   ▓██▒▒██████▒▒░▒████▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒   ▒██░   ▓██░▒██▒ █▄░██▓ ▒██▒▒███████▒ ██▓ ░▒████▓ ░██████▒░██████▒
▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░░▒▓███▀▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░░ ▒░ ░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░   ░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒░ ▒▓ ░▒▓░░▒▒ ▓░▒░▒ ▒▓▒  ▒▒▓  ▒ ░ ▒░▓  ░░ ▒░▓  ░
░ ░▒  ░ ░░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒  ░ ░▒░▒   ░   ▒   ▒▒ ░░ ░▒  ░ ░ ░ ░  ░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░   ░ ░░   ░ ▒░░ ░▒ ▒░  ░▒ ░ ▒░░░▒ ▒ ░ ▒ ░▒   ░ ▒  ▒ ░ ░ ▒  ░░ ░ ▒  ░
░  ░  ░     ░   ░ ░  ░░░ ░ ░ ░  ░  ░   ░    ░   ░   ▒   ░  ░  ░     ░        ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░         ░   ░ ░ ░ ░░ ░   ░░   ░ ░ ░ ░ ░ ░ ░    ░ ░  ░   ░ ░     ░ ░   
      ░           ░    ░           ░   ░            ░  ░      ░     ░  ░                ░ ░      ░ ░      ░  ░            ░ ░  ░      ░       ░ ░      ░     ░        ░  ░    ░  ░
                                            ░                                                                                               ░          ░   ░                      

'''))
    driver = setup_driver()
    driver.get('https://snusbase.com/')
    
    add_cookies(driver)
    driver.refresh()
    time.sleep(10)

if __name__ == "__main__":
    main()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')