import requests
import fade
import time

def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)
    print()

def print_banner():
    banner = """
 ▄████▄    █████▒▒██   ██▒    ██▓     ▒█████   ▒█████   ██ ▄█▀ █    ██  ██▓███  
▒██▀ ▀█  ▓██   ▒ ▒▒ █ █ ▒░   ▓██▒    ▒██▒  ██▒▒██▒  ██▒ ██▄█▒  ██  ▓██▒▓██░  ██▒
▒▓█    ▄ ▒████ ░ ░░  █   ░   ▒██░    ▒██░  ██▒▒██░  ██▒▓███▄░ ▓██  ▒██░▓██░ ██▓▒
▒▓▓▄ ▄██▒░▓█▒  ░  ░ █ █ ▒    ▒██░    ▒██   ██░▒██   ██░▓██ █▄ ▓▓█  ░██░▒██▄█▓▒ ▒
▒ ▓███▀ ░░▒█░    ▒██▒ ▒██▒   ░██████▒░ ████▓▒░░ ████▓▒░▒██▒ █▄▒▒█████▓ ▒██▒ ░  ░
░ ░▒ ▒  ░ ▒ ░    ▒▒ ░ ░▓ ░   ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
  ░  ▒    ░      ░░   ░▒ ░   ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░░░▒░ ░ ░ ░▒ ░     
░         ░ ░     ░    ░       ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░  ░░░ ░ ░ ░░       
░ ░               ░    ░         ░  ░    ░ ░      ░ ░  ░  ░      ░              
░                                                                                 
    """
    Slow(fade.water(banner))

def get_fivem_server_info(cfx_id):
    url = f"https://servers-frontend.fivem.net/api/servers/single/{cfx_id}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        server_info = response.json()

        data = {
            "Server Name": server_info.get('Data', {}).get('hostname', 'Unavailable'),
            "IP": server_info.get('Data', {}).get('connectEndPoints', ['Unavailable'])[0].split(':')[0],
            "Port": server_info.get('Data', {}).get('connectEndPoints', ['Unavailable'])[0].split(':')[1],
        }

        return data
    except requests.exceptions.RequestException as e:
        return {"Error": str(e)}

def main():
    print_banner()
    cfx_id = input(fade.water("Enter the CFX ID of the server: "))
    server_data = get_fivem_server_info(cfx_id)
    
    if "Error" in server_data:
        Slow(fade.water(f"Error: {server_data['Error']}"))
    else:
        Slow(fade.water("Server Information:"))
        for key, value in server_data.items():
            Slow(fade.water(f"{key}: {value}"))

if __name__ == "__main__":
    main()
    import os    
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')