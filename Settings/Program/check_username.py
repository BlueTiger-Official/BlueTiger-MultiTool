import requests
from requests.exceptions import HTTPError, SSLError, RequestException
import re

def check_username(username):
    if not username:
        print("**Invalid Username.** \nExample: Abcdef")
        return

    sites = [
        f"https://github.com/{username}",
        f"https://www.facebook.com/{username}",
        f"https://www.linkedin.com/in/{username}",
        f"https://linktr.ee/{username}",
        f"https://www.snapchat.com/add/{username}",
        f"https://twitter.com/{username}",
        f"https://instagram.com/{username}",
        f"https://www.reddit.com/user/{username}",
        f"https://www.pinterest.com/{username}",
        f"https://www.twitch.tv/{username}",
        f"https://open.spotify.com/user/{username}",
        f"https://www.roblox.com/user.aspx?username={username}",
        f"https://t.me/{username}",
        f"https://xvideos.com/profiles/{username}",
        f"https://www.youtube.com/@{username}",
        f"https://api.mojang.com/users/profiles/minecraft/{username}",
        f"https://www.codewars.com/users/{username}",
        f"https://forum.hackthebox.com/profile/{username}",
        f"https://replit.com/@{username}",
        f"https://www.chess.com/member/{username}",
        f"https://www.behance.net/{username}",
        f"https://www.soundcloud.com/{username}",
        f"https://www.dribbble.com/{username}",
        f"https://www.deviantart.com/{username}",
        f"https://www.producthunt.com/@{username}"
    ]

    valid_users = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    for url in sites:
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                if re.search(username, response.text, re.IGNORECASE):
                    valid_users.append(url)
            elif response.status_code in [404, 406]:
                continue
        except HTTPError as e:
            print(f"HTTPError pour {url}: {e}")
        except SSLError as e:
            print(f"SSLError pour {url}: {e}")
        except RequestException as e:
            print(f"RequestException pour {url}: {e}")

    if valid_users:
        print("Résultats de la vérification :")
        for index, user_url in enumerate(valid_users, start=1):
            print(f"Utilisateur {index}: {user_url}")
    else:
        print("Aucun utilisateur valide trouvé.")

if __name__ == "__main__":
    username = input("Entrez le nom d'utilisateur à vérifier : ")
    check_username(username)
    import os    
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
