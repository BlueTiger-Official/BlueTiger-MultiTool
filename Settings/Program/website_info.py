import socket
import requests
import time
import os
import fade

IPINFO_API_KEY = '66819ffdf72438'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)
    print()

def resolve_ip_from_url(url):
    try:
        ip = socket.gethostbyname(url)
        return ip
    except socket.error as e:
        Slow(f"Error resolving IP address for {url}: {e}")
        return None

def get_ipinfo(ip):
    url = f'https://ipinfo.io/{ip}/json?token={IPINFO_API_KEY}'
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        Slow(f"Failed to retrieve data from IPinfo for IP: {ip}")
        return None

def display_website_info(ip):
    data = get_ipinfo(ip)
    
    if data:
        Slow(f"IP Address: {data.get('ip', 'Unknown')}")
        Slow(f"Organization: {data.get('org', 'Unknown')}")
        Slow(f"Hostname: {data.get('hostname', 'Unknown')}")
        Slow(f"Location: {data.get('city', 'Unknown')}, {data.get('region', 'Unknown')}, {data.get('country', 'Unknown')}")
        Slow(f"ISP: {data.get('isp', 'Unknown')}")
        Slow(f"Location Coordinates: {data.get('loc', 'Unknown')}")
    else:
        Slow("No information found or failed to retrieve data.")

def main():
    clear()
    url = input("Enter website URL to get info: ").strip()
    ip = resolve_ip_from_url(url)
    
    if ip:
        Slow(f"Fetching information for IP: {ip}...")
        display_website_info(ip)
    else:
        Slow("Failed to resolve IP address for the given URL.")

if __name__ == "__main__":
    main()

    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
