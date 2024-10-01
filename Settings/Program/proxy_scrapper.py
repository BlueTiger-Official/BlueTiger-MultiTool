import requests, itertools, os, fade, time
from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup
import os

def Slow(texte):
    for line in texte.splitlines():
        print(line)
        time.sleep(0.05)

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def error(text):
    Slow(fade.water(f'\n[*] Unexpected error in ProxyCheck: {text}'))
    input(fade.water(f'[*] Press ENTER to return the menu: '))
    start()

def get_proxies_from_web():
    urls = [
        'https://www.sslproxies.org/',
        'https://free-proxy-list.net/',
        'https://www.us-proxy.org/',
    ]
    proxies = set()
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find(id='proxylisttable')
            if table:
                rows = table.find('tbody').find_all('tr')
                for row in rows:
                    tds = row.find_all('td')
                    ip = tds[0].text
                    port = tds[1].text
                    protocol = tds[6].text.lower()
                    if 'socks' in protocol:
                        proxies.add(f"{protocol}://{ip}:{port}")
                    else:
                        proxies.add(f"http://{ip}:{port}")
        except Exception as e:
            error(f'Error scraping {url}: {e}')
    return proxies

def get_proxies_from_github():
    urls = [
        'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
        'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
        'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt'
    ]
    proxies = set()
    for url in urls:
        try:
            response = requests.get(url)
            proxies.update(response.text.splitlines())
        except Exception as e:
            error(f'Error fetching proxies from GitHub: {e}')
    return proxies

def check_proxy(proxy):
    protocol = proxy.split("://")[0]
    proxies = {
        "http": f"http://{proxy}",
        "https": f"https://{proxy}"
    } if protocol in ["http", "https"] else {
        "socks4": f"socks4://{proxy}",
        "socks5": f"socks5://{proxy}"
    }
    
    try:
        if protocol in ["http", "https"]:
            response = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=5)
        else:
            response = requests.get("http://httpbin.org/ip", proxies={protocol: proxy}, timeout=5)
        
        if response.status_code == 200:
            return proxy, True
    except:
        return proxy, False
    return proxy, False

def main(max_proxies_to_check=100):
    all_proxies = get_proxies_from_web().union(get_proxies_from_github())
    proxies_to_check = list(itertools.islice(all_proxies, max_proxies_to_check))
    
    valid_proxies = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(check_proxy, proxy): proxy for proxy in proxies_to_check}
        for future in as_completed(futures):
            proxy = futures[future]
            try:
                proxy, is_valid = future.result()
                if is_valid:
                    valid_proxies.append(proxy)
                    Slow(fade.water(f"[*] Valid proxy found: [{proxy}]"))
                    with open("valid-proxies.txt", "a") as file:
                        file.write(f"{proxy}\n")
                else:
                    Slow(fade.water(f"[*] Invalid proxy found: [{proxy}]"))
            except Exception as exc:
                print(f"Generated an exception: {exc}")

def start():
    clear()
    title = '''
 ██▓███   ██▀███   ▒█████  ▒██   ██▒▓██   ██▓     ██████  ▄████▄   ██▀███   ▄▄▄       ██▓███  
▓██░  ██▒▓██ ▒ ██▒▒██▒  ██▒▒▒ █ █ ▒░ ▒██  ██▒   ▒██    ▒ ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▓██░  ██▒
▓██░ ██▓▒▓██ ░▄█ ▒▒██░  ██▒░░  █   ░  ▒██ ██░   ░ ▓██▄   ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▓██░ ██▓▒
▒██▄█▓▒ ▒▒██▀▀█▄  ▒██   ██░ ░ █ █ ▒   ░ ▐██▓░     ▒   ██▒▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒██▄█▓▒ ▒
▒██▒ ░  ░░██▓ ▒██▒░ ████▓▒░▒██▒ ▒██▒  ░ ██▒▓░   ▒██████▒▒▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒██▒ ░  ░
▒▓▒░ ░  ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ▒▒ ░ ░▓ ░   ██▒▒▒    ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒▓▒░ ░  ░
░▒ ░       ░▒ ░ ▒░  ░ ▒ ▒░ ░░   ░▒ ░ ▓██ ░▒░    ░ ░▒  ░ ░  ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░░▒ ░     
░░         ░░   ░ ░ ░ ░ ▒   ░    ░   ▒ ▒ ░░     ░  ░  ░  ░          ░░   ░   ░   ▒   ░░       
            ░         ░ ░   ░    ░   ░ ░              ░  ░ ░         ░           ░  ░         
                                     ░ ░                 ░                                    
'''
    Slow(fade.fire(title))
    choice = int(input(fade.water('[*] Enter the number of proxies to scrape and check: ')))
    print('\n')
    main(max_proxies_to_check=choice) 

if __name__ == "__main__":
    start()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
