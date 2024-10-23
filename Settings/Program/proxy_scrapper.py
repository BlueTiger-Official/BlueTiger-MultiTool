import requests
import threading
import time
import re
import os
from colorama import init, Fore

def Slow(texte):
    for line in texte.splitlines():
        Slow(line)
        time.sleep(0.05)

class ProxyHandler():
    def __init__(self, output_directory: str, filename: str):
        self.output_directory = output_directory
        self.filename = filename
        self.proxies = []
        self.valid_proxies = []

        os.makedirs(self.output_directory, exist_ok=True)

    banner = """
    

 ██▓███   ██▀███   ▒█████  ▒██   ██▒▓██   ██▓     ██████  ▄████▄   ██▀███   ▄▄▄       ██▓███   ██▓███  ▓█████  ██▀███  
▓██░  ██▒▓██ ▒ ██▒▒██▒  ██▒▒▒ █ █ ▒░ ▒██  ██▒   ▒██    ▒ ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▓██░  ██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
▓██░ ██▓▒▓██ ░▄█ ▒▒██░  ██▒░░  █   ░  ▒██ ██░   ░ ▓██▄   ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▓██░ ██▓▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
▒██▄█▓▒ ▒▒██▀▀█▄  ▒██   ██░ ░ █ █ ▒   ░ ▐██▓░     ▒   ██▒▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒██▄█▓▒ ▒▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  
▒██▒ ░  ░░██▓ ▒██▒░ ████▓▒░▒██▒ ▒██▒  ░ ██▒▓░   ▒██████▒▒▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒██▒ ░  ░▒██▒ ░  ░░▒████▒░██▓ ▒██▒
▒▓▒░ ░  ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ▒▒ ░ ░▓ ░   ██▒▒▒    ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒▓▒░ ░  ░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
░▒ ░       ░▒ ░ ▒░  ░ ▒ ▒░ ░░   ░▒ ░ ▓██ ░▒░    ░ ░▒  ░ ░  ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░░▒ ░     ░▒ ░      ░ ░  ░  ░▒ ░ ▒░
░░         ░░   ░ ░ ░ ░ ▒   ░    ░   ▒ ▒ ░░     ░  ░  ░  ░          ░░   ░   ░   ▒   ░░       ░░          ░     ░░   ░ 
            ░         ░ ░   ░    ░   ░ ░              ░  ░ ░         ░           ░  ░                     ░  ░   ░     
                                     ░ ░                 ░                                                             
                                     									 
"""
    Slow(banner)

    def scrape_proxies(self):
        urls = """
        https://api.openproxylist.xyz/http.txt
        https://api.proxyscrape.com/v2/?request=getproxies&protocol=http
        https://api.proxyscrape.com/v2/?request=getproxies&protocol=https
        https://openproxy.space/list/http
        https://proxyspace.pro/http.txt
        https://proxyspace.pro/https.txt
        https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt
        https://raw.githubusercontent.com/andigwandi/free-proxy/main/proxy_list.txt
        https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt
        https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt
        https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt
        https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt
        https://raw.githubusercontent.com/elliottophellia/yakumo/master/results/http/global/http_checked.txt
        https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt
        https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt
        https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt
        https://raw.githubusercontent.com/im-razvan/proxy_list/main/http.txt
        https://raw.githubusercontent.com/Master-Mind-007/Auto-Parse-Proxy/main/https.txt
        https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt
        https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt
        https://raw.githubusercontent.com/MrMarble/proxy-list/main/all.txt
        https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt
        https://raw.githubusercontent.com/NotUnko/autoproxies/main/proxies/https
        https://raw.githubusercontent.com/ObcbO/getproxy/master/file/http.txt
        https://raw.githubusercontent.com/ObcbO/getproxy/master/file/https.txt
        https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt
        https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt
        https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/data.txt
        https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt
        https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt
        https://raw.githubusercontent.com/r00tee/Proxy-List/main/Https.txt
        https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt
        https://raw.githubusercontent.com/Sage520/Proxy-List/main/http.txt
        https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/free.txt
        https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt
        https://raw.githubusercontent.com/themiralay/Proxy-List-World/master/data.txt
        https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt
        https://raw.githubusercontent.com/Tsprnay/Proxy-lists/master/proxies/http.txt
        https://raw.githubusercontent.com/Tsprnay/Proxy-lists/master/proxies/https.txt
        https://raw.githubusercontent.com/tuanminpay/live-proxy/master/http.txt
        https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt
        https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/https.txt
        https://raw.githubusercontent.com/Vann-Dev/proxy-list/main/proxies/http.txt
        https://raw.githubusercontent.com/Vann-Dev/proxy-list/main/proxies/https.txt
        https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/http.txt
        https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt
        https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt
        https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt
        https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt
        https://raw.githubusercontent.com/zloi-user/hideip.me/main/https.txt
        https://www.proxy-list.download/api/v1/get?type=http
        https://www.proxy-list.download/api/v1/get?type=https
        https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&proxy_format=protocolipport&format=text&timeout=20000
        https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt
        https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt
        https://raw.githubusercontent.com/a2u/free-proxy-list/master/free-proxy-list.txt
        https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt
        https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt
        https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt
        https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt
        https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS5.txt
        https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks5.txt
        https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt
        https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks5.txt
        https://api.openproxylist.xyz/socks5.txt
        https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5
        https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5
        https://proxyspace.pro/socks5.txt
        https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt
        https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt
        https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks5.txt
        https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt
        https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt
        https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt
        https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt
        https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt
        https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt
        https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/socks5.txt
        https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks5.txt
        https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks5.txt
        https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks5.txt
        https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/socks5.txt
        https://raw.githubusercontent.com/YuvalKatzav/Socks-Proxy/main/SOCKS5.txt
        https://raw.githubusercontent.com/YuvalKatzav/Socks-Proxy/main/SOCKS4.txt
        https://raw.githubusercontent.com/zhangwenxuan007/Free-Proxy-List/master/socks4.txt
        https://raw.githubusercontent.com/zhangwenxuan007/Free-Proxy-List/master/socks5.txt
        https://raw.githubusercontent.com/zhenboy123/proxylist/master/socks4.txt
        https://raw.githubusercontent.com/zhenboy123/proxylist/master/socks5.txt
        https://raw.githubusercontent.com/zhenboy123/proxylist/master/http.txt
        """.strip().splitlines()

        for url in urls:
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    proxies = response.text.splitlines()
                    for proxy in proxies:
                        if proxy not in self.proxies:
                            self.proxies.append(proxy)
                    Slow(Fore.GREEN + f"Proxies scraped from {url}")
            except requests.RequestException as e:
                Slow(Fore.RED + f"Failed to fetch from {url}: {e}")

    def check_proxies(self):
        Slow(Fore.CYAN + "Checking proxies...")
        threads = []
        lock = threading.Lock()

        def worker(proxy):
            try:
                response = requests.get("http://httpbin.org/ip", proxies={"http": proxy, "https": proxy}, timeout=5)
                if response.status_code == 200:
                    with lock:
                        self.valid_proxies.append(proxy)
                        Slow(Fore.GREEN + f"Valid proxy found: {proxy}")
                else:
                    Slow(Fore.RED + f"Invalid proxy: {proxy}")
            except requests.RequestException:
                Slow(Fore.RED + f"Invalid proxy: {proxy}")

        for proxy in self.proxies:
            thread = threading.Thread(target=worker, args=(proxy,))
            thread.start()
            threads.append(thread)
            time.sleep(0.1) 

        for thread in threads:
            thread.join()

    def sort_proxies(self):
        Slow(Fore.CYAN + "Sorting proxies...")
        patterns = {
            'socks4': r':[0-9]+$',
            'socks5': r':[0-9]+$',
            'http': r':80$|:[0-9]{4}$',
            'https': r':443$|:[0-9]{4}$'
        }

        output_files = {
            'socks4': os.path.join(self.output_directory, 'socks4_proxies.txt'),
            'socks5': os.path.join(self.output_directory, 'socks5_proxies.txt'),
            'http': os.path.join(self.output_directory, 'http_proxies.txt'),
            'https': os.path.join(self.output_directory, 'https_proxies.txt')
        }

        for proxy in self.valid_proxies:
            for proxy_type, pattern in patterns.items():
                if re.search(pattern, proxy):
                    with open(output_files[proxy_type], 'a') as f:
                        f.write(proxy + '\n')
                    break

        Slow(Fore.GREEN + "Proxies sorted and saved.")

    def save_proxies(self):
        with open(os.path.join(self.output_directory, self.filename), "w") as file:
            for proxy in self.valid_proxies:
                file.write(proxy + "\n")
        Slow(Fore.GREEN + f"Proxies saved to {self.output_directory}/{self.filename}")


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    proxy_handler = ProxyHandler("./Output", "proxy.txt")
    proxy_handler.scrape_proxies()
    proxy_handler.check_proxies()
    proxy_handler.sort_proxies()
    proxy_handler.save_proxies()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
