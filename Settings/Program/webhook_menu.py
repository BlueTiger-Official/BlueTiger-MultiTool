import requests
import time
import fade
import os
import json

def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)
    print()

def send_webhook_message(webhook_url, username, message, num_messages, cooldown, avatar_url=None):
    payload = {
        'username': username,
        'content': message,
        'avatar_url': avatar_url
    }
    Slow(fade.water("""
    Spamming..."""))

    for _ in range(num_messages):
        requests.post(webhook_url, json=payload)
        time.sleep(cooldown)

    Slow(fade.water("""
    Spamming done."""))

def delete_webhook(webhook_url):
    requests.delete(webhook_url)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_webhook_info(webhook_url):
    try:
        response = requests.get(webhook_url)
        if response.status_code == 200:
            webhook_data = response.json()
            Slow(fade.water("Webhook Information:"))
            Slow(fade.water(f"Webhook Name: {webhook_data['name']}"))
            Slow(fade.water(f"Created by: {webhook_data['user']['username']}"))

            if 'guild_id' in webhook_data and 'channel_id' in webhook_data:
                guild_id = webhook_data['guild_id']
                channel_id = webhook_data['channel_id']
                Slow(fade.water(f"Server ID : {guild_id}"))
                Slow(fade.water(f"Channel ID: {channel_id}"))
            else:
                Slow(fade.water("Server and Channel information not available."))
        else:
            Slow(fade.water("Unable to retrieve webhook information. Make sure the URL is correct."))
    except Exception as e:
        Slow(fade.water(f"An error occurred: {str(e)}"))

def return_to_menu():
    input(fade.water("\nPress Enter to return to the menu."))
    clear_console()
    show_menu()

def exit_program():
    clear_console()
    Slow(fade.water("Exiting the program."))
    os.system('python ../../main.py')

def show_menu():
    clear_console()
    Slow(fade.water("""
 █     █░▓█████  ▄▄▄▄    ██░ ██  ▒█████   ▒█████   ██ ▄█▀   ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
▓█░ █ ░█░▓█   ▀ ▓█████▄ ▓██░ ██▒▒██▒  ██▒▒██▒  ██▒ ██▄█▒    ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
▒█░ █ ░█ ▒███   ▒██▒ ▄██▒██▀▀██░▒██░  ██▒▒██░  ██▒▓███▄░    ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀  ░▓█ ░██ ▒██   ██░▒██   ██░▓██ █▄    ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
░░██▒██▓ ░▒████▒░▓█  ▀█▓░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ █▄     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
  ▒ ░ ░   ░ ░  ░▒░▒   ░  ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
  ░   ░     ░    ░    ░  ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░      ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
    ░       ░  ░ ░       ░  ░  ░    ░ ░      ░ ░  ░  ░                   ░ ░      ░ ░      ░  ░
                      ░                                                                        

"""))

    menu_choice = input(fade.water("""
                                 [1] Spam the webhook
                                 [2] Delete the webhook
                                 [3] Webhook information
                                 [4] Quit
                                 
  Enter your choice: """))

    if menu_choice == "1":
        webhook_url = input(fade.water("Webhook URL: "))
        username = input(fade.water("Webhook Name: "))
        message = input(fade.water("Message: "))
        num_messages = int(input(fade.water("How many messages: ")))
        cooldown = int(input(fade.water("Cooldown (0 = no cooldown): ")))
        avatar_url = input(fade.water("Avatar link: "))

        send_webhook_message(webhook_url, username, message, num_messages, cooldown, avatar_url)
        return_to_menu()

    elif menu_choice == "2":
        webhook_url = input(fade.water("Webhook URL: "))
        delete_webhook(webhook_url)
        Slow(fade.water("Webhook deleted."))
        return_to_menu()

    elif menu_choice == "3":
        webhook_url = input(fade.water("Webhook URL: "))
        get_webhook_info(webhook_url)
        return_to_menu()

    elif menu_choice == "4":
        exit_program()

    else:
        Slow(fade.water("Invalid choice."))
        return_to_menu()

show_menu()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')