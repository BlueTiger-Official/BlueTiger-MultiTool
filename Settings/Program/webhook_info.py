import requests
import os
import time
import fade

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)
    print()

def info_webhook(webhook_url):
    headers = {
        'Content-Type': 'application/json',
    }

    try:
        response = requests.get(webhook_url, headers=headers)
        response.raise_for_status()
        webhook_info = response.json()
        clear()
        Slow("\nInformation Webhook:")

        Slow(f"ID : {webhook_info['id']}")
        Slow(f"Token : {webhook_info['token']}")
        Slow(f"Name : {webhook_info['name']}")
        Slow(f"Avatar : {webhook_info['avatar']}")
        Slow(f"Type  : {'bot' if webhook_info['type'] == 1 else 'webhook utilisateur'}")
        Slow(f"Channel ID : {webhook_info['channel_id']}")
        Slow(f"Server ID  : {webhook_info['guild_id']}")

        Slow("\nUser information associated with the Webhook:")
        if 'user' in webhook_info and webhook_info['user']:
            user_info = webhook_info['user']
            Slow(f"ID : {user_info['id']}")
            Slow(f"Name : {user_info['username']}")
            Slow(f"DisplayName : {user_info.get('global_name', 'N/A')}")
            Slow(f"Number : {user_info['discriminator']}")
            Slow(f"Avatar : {user_info['avatar']}")
            Slow(f"Flags : {user_info['flags']} Publique: {user_info['public_flags']}")
            Slow(f"Color : {user_info.get('accent_color', 'N/A')}")
            Slow(f"Decoration : {user_info.get('avatar_decoration_data', 'N/A')}")
            Slow(f"Banner : {user_info.get('banner_color', 'N/A')}")
            Slow("")
        else:
            Slow("\nNo user information associated with the Webhook.")

    except requests.exceptions.RequestException as e:
        Slow(f"[ERROR] {e}")

if __name__ == "__main__":
    clear()
    webhook_url = input("Enter Webhook URL: ")
    info_webhook(webhook_url)

    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
