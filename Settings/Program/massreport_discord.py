import requests
import threading
import os
import fade
import time
import sys

DEFAULT_REPORT_REASON = "Inappropriate content"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)
    print()

def print_ascii_art():
    art = """
 ███▄ ▄███▓ ▄▄▄        ██████   ██████     ██▀███  ▓█████  ██▓███   ▒█████   ██▀███  ▄▄▄█████▓
▓██▒▀█▀ ██▒▒████▄    ▒██    ▒ ▒██    ▒    ▓██ ▒ ██▒▓█   ▀ ▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒
▓██    ▓██░▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄      ▓██ ░▄█ ▒▒███   ▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░
▒██    ▒██ ░██▄▄▄▄██   ▒   ██▒  ▒   ██▒   ▒██▀▀█▄  ▒▓█  ▄ ▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░ 
▒██▒   ░██▒ ▓█   ▓██▒▒██████▒▒▒██████▒▒   ░██▓ ▒██▒░▒████▒▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░ 
░ ▒░   ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░   ░ ▒▓ ░▒▓░░░ ▒░ ░▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░   
░  ░      ░  ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░     ░▒ ░ ▒░ ░ ░  ░░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░    
░      ░     ░   ▒   ░  ░  ░  ░  ░  ░       ░░   ░    ░   ░░       ░ ░ ░ ▒    ░░   ░   ░      
       ░         ░  ░      ░        ░        ░        ░  ░             ░ ░     ░              
                                                                                                
                                                                              
    """
    Slow(art)

def MassReport(token, guild_id, channel_id, message_id, reason):
    for _ in range(500):
        threading.Thread(target=Report, args=(token, guild_id, channel_id, message_id, reason)).start()

def Report(token, guild_id, channel_id, message_id, reason):
    url = 'https://discordapp.com/api/v8/report'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'User-Agent': 'Discord/21295 CFNetwork/1128.0.1 Darwin/19.6.0',
        'Content-Type': 'application/json',
        'Authorization': token
    }
    payload = {
        'channel_id': channel_id,
        'message_id': message_id,
        'guild_id': guild_id,
        'reason': reason
    }

    response = requests.post(url, json=payload, headers=headers)
    
    status = response.status_code
    response_message = response.json().get('message', 'Unknown error')

    if status == 201:
        Slow("Report successfully sent!")
    elif status in (401, 403):
        Slow(f"{response_message}")
    else:
        Slow(f"Error: {response_message} | Status Code: {status}")

if __name__ == "__main__":
    clear()
    print_ascii_art()
    Slow("Enter your Discord token (its for reporting): ")
    token = input().strip()
    Slow("Enter the server ID: ")
    guild_id = input().strip()
    Slow("Enter the channel ID: ")
    channel_id = input().strip()
    Slow("Enter the message ID: ")
    message_id = input().strip()
    
    Slow(f"Enter the report reason (default: {DEFAULT_REPORT_REASON}): ")
    reason = input().strip()
    if not reason:
        reason = DEFAULT_REPORT_REASON

    MassReport(token, guild_id, channel_id, message_id, reason)
        input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
