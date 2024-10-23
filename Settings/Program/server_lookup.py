import requests
from colorama import Fore
import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def setTitle(title):
    print(f"Setting title to: {title}")

def Slow(texte):
    for line in texte.splitlines():
        print(line)
        time.sleep(0.05)

def serverlookuptitle():
    Slow("""
  ██████ ▓█████  ██▀███   ██▒   █▓▓█████  ██▀███      ██▓     ▒█████   ▒█████   ██ ▄█▀ █    ██  ██▓███  
▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒   ▓██▒    ▒██▒  ██▒▒██▒  ██▒ ██▄█▒  ██  ▓██▒▓██░  ██▒
░ ▓██▄   ▒███   ▓██ ░▄█ ▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒   ▒██░    ▒██░  ██▒▒██░  ██▒▓███▄░ ▓██  ▒██░▓██░ ██▓▒
  ▒   ██▒▒▓█  ▄ ▒██▀▀█▄    ▒██ █░░▒▓█  ▄ ▒██▀▀█▄     ▒██░    ▒██   ██░▒██   ██░▓██ █▄ ▓▓█  ░██░▒██▄█▓▒ ▒
▒██████▒▒░▒████▒░██▓ ▒██▒   ▒▀█░  ░▒████▒░██▓ ▒██▒   ░██████▒░ ████▓▒░░ ████▓▒░▒██▒ █▄▒▒█████▓ ▒██▒ ░  ░
▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░   ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░   ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░   ░ ░░   ░ ░  ░  ░▒ ░ ▒░   ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░░░▒░ ░ ░ ░▒ ░     
░  ░  ░     ░     ░░   ░      ░░     ░     ░░   ░      ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░  ░░░ ░ ░ ░░       
      ░     ░  ░   ░           ░     ░  ░   ░            ░  ░    ░ ░      ░ ░  ░  ░      ░              
                              ░                                                                             
                                                              
""")

def serverlookup():
    clear()
    serverlookuptitle()
    Slow(f"""{Fore.LIGHTBLUE_EX}#{Fore.LIGHTYELLOW_EX} You can find: \n\n""")
    Slow(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Invite Link           {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Inviter Username      {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Guild Banner          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Guild Splash\n""")
    Slow(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Channel Name          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Inviter ID            {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Guild Description     {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Guild Features\n""")
    Slow(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Channel ID            {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Guild Name            {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Custom Invite Link\n""")
    Slow(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Expiration Date       {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Guild ID              {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Verification Level\n\n\n\n""")
    
    invitelink = input(f"{Fore.LIGHTBLUE_EX}~{Fore.LIGHTYELLOW_EX} Insert end part of link of discord server link: ")
    clear()
    
    try:
        if "discord.gg" in invitelink:
            code = invitelink.split('/')[-1]
        else:
            code = invitelink
            
        res = requests.get(f"https://discord.com/api/v9/invites/{code}")
        
        if res.status_code == 200:
            res_json = res.json()

            Slow(f"""\n{Fore.LIGHTBLUE_EX}#{Fore.LIGHTYELLOW_EX} Invitation Information:""")
            Slow(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Invite Link: {f'https://discord.gg/{res_json["code"]}'}""")
            Slow(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Channel: {res_json["channel"]["name"]} ({res_json["channel"]["id"]})""")
            Slow(f"""                    {Fore.LIGHTYELLOW_EX}+{Fore.LIGHTBLUE_EX} Expiration Date: {res_json["expires_at"]}\n""")

            Slow(f"""{Fore.LIGHTBLUE_EX}#{Fore.LIGHTYELLOW_EX} Inviter Information:""")
            Slow(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Username: {f'{res_json["inviter"]["username"]}#{res_json["inviter"]["discriminator"]}'}""")
            Slow(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} User ID: {res_json["inviter"]["id"]}\n""")

            Slow(f"""{Fore.LIGHTBLUE_EX}#{Fore.LIGHTYELLOW_EX} Server Information:""")
            Slow(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Name: {res_json["guild"]["name"]}""")
            Slow(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Server ID: {res_json["guild"]["id"]}""")
            Slow(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Banner: {res_json["guild"]["banner"]}""")
            Slow(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Description: {res_json["guild"]["description"]}""")
            Slow(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Custom Invite Link: {res_json["guild"]["vanity_url_code"]}""")
            Slow(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Verification Level: {res_json["guild"]["verification_level"]}""")
            Slow(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Splash: {res_json["guild"]["splash"]}""")
            Slow(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Features: {res_json["guild"]["features"]}""")
        else:
            input(f"""          {Fore.LIGHTYELLOW_EX}~{Fore.LIGHTBLUE_EX} An error occurred while sending request""")
            return

    except Exception as e:
        Slow(f"Error: {e}")
        input(f"Press ENTER to exit")
        return
    
    input(f"""{Fore.LIGHTBLUE_EX}~{Fore.LIGHTYELLOW_EX} Press ENTER to exit""")

def main():
    setTitle("Server Lookup")
    serverlookup()

if __name__ == "__main__":
    main()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')