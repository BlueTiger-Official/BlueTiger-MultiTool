import os
import socket
import requests
import time
from pystyle import Colors, Colorate


def Slow(texte):
    for line in texte.splitlines():
        print(line)
        time.sleep(0.05)


def Continue():
    input(Colorate.Horizontal(Colors.blue_to_red, "\nPress Enter to continue..."))


def Reset():
    os.system('cls' if os.name == 'nt' else 'clear')


def ErrorModule(e):
    Slow(Colorate.Horizontal(Colors.red_to_yellow, f"Error importing module: {e}"))


def Error(e):
    Slow(Colorate.Horizontal(Colors.red_to_yellow, f"An error occurred: {e}"))


def current_time_hour():
    return time.strftime("%H:%M:%S")


ascii_art = """
  ██████  ██▓▄▄▄█████▓▓█████      ██████  ▄████▄   ▄▄▄       ███▄    █  ███▄    █ ▓█████  ██▀███  
▒██    ▒ ▓██▒▓  ██▒ ▓▒▓█   ▀    ▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▒██▒▒ ▓██░ ▒░▒███      ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
  ▒   ██▒░██░░ ▓██▓ ░ ▒▓█  ▄      ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒░██░  ▒██▒ ░ ░▒████▒   ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░▓    ▒ ░░   ░░ ▒░ ░   ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░ ▒ ░    ░     ░ ░  ░   ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
░  ░  ░   ▒ ░  ░         ░      ░  ░  ░  ░          ░   ▒      ░   ░ ░    ░   ░ ░    ░     ░░   ░ 
      ░   ░              ░  ░         ░  ░ ░            ░  ░         ░          ░    ░  ░   ░     
                                         ░                                                            
"""

Slow(Colorate.Horizontal(Colors.blue_to_red, ascii_art))

try:
    def domain_scan(website_url):
        domain = website_url.replace("https://", "").replace("http://", "").split('/')[0]
        return domain

    def secure_scan(website_url):
        return website_url.startswith("https://")

    def status_scan(website_url):
        response = requests.get(website_url)
        return response.status_code

    def ip_scan(domain):
        try:
            ip = socket.gethostbyname(domain)
        except Exception as e:
            ErrorModule(e)
            ip = "None"

        try:
            response = requests.get(f"https://{domain}/api/ip/ip={ip}")
            api = response.json()
            status = api.get('status', 'Invalid')
            host_isp = api.get('isp', 'None')
            host_org = api.get('org', 'None')
            host_as = api.get('as', 'None')
        except Exception as e:
            ErrorModule(e)
            status = "Invalid"
            host_isp = "None"
            host_org = "None"
            host_as = "None"

        return ip, status, host_isp, host_org, host_as

    def port_scan(ip):
        open_ports = []
        common_ports = {
            80: "HTTP",
            443: "HTTPS",
            21: "FTP",
            22: "SSH",
            25: "SMTP",
            53: "DNS",
            110: "POP3",
            143: "IMAP",
            3306: "MySQL",
            5432: "PostgreSQL",
            6379: "Redis",
            27017: "MongoDB",
            8080: "HTTP-alt"
        }

        for port, service in common_ports.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            try:
                result = sock.connect_ex((ip, port))
                if result == 0:
                    open_ports.append((port, service))
            except Exception as e:
                ErrorModule(e)
            finally:
                sock.close()

        return ' / '.join([f'{port}/{service}' for port, service in open_ports])

    website_url = input(Colorate.Horizontal(Colors.blue_to_red, f"\n{current_time_hour()} Website Url -> "))
    Slow(Colorate.Horizontal(Colors.blue_to_red, f"{current_time_hour()} Scanning...\n"))

    if "https://" not in website_url and "http://" not in website_url:
        website_url = "https://" + website_url

    Slow(Colorate.Horizontal(Colors.blue_to_red, f"Website : {website_url}"))

    domain = domain_scan(website_url)
    Slow(Colorate.Horizontal(Colors.blue_to_red, f"Domain : {domain}"))

    secure = secure_scan(website_url)
    Slow(Colorate.Horizontal(Colors.blue_to_red, f"Secure : {secure}"))

    status_code = status_scan(website_url)
    Slow(Colorate.Horizontal(Colors.blue_to_red, f"Status Code : {status_code}"))

    ip, ip_status, host_isp, host_org, host_as = ip_scan(domain)
    Slow(Colorate.Horizontal(Colors.blue_to_red, f"Ip : {ip}"))
    Slow(Colorate.Horizontal(Colors.blue_to_red, f"Ip Status : {ip_status}"))
    Slow(Colorate.Horizontal(Colors.blue_to_red, f"Host Isp : {host_isp}"))
    Slow(Colorate.Horizontal(Colors.blue_to_red, f"Host Org : {host_org}"))
    Slow(Colorate.Horizontal(Colors.blue_to_red, f"Host As     : {host_as}"))

    open_ports = port_scan(ip)
    Slow(Colorate.Horizontal(Colors.blue_to_red, f"Open Ports  : {open_ports}"))

    print()
    Continue()
    Reset()

except Exception as e:
    Error(e)

input("[x] Appuyer sur entrée pour retourner au menu principal.")
os.system('python ../../main.py')
