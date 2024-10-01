import requests
import json
from datetime import datetime
import fade
import time
import os
import sys


def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)
    print()


def get_tiktok_user_info(username) -> dict:
    url = f'https://www.tiktok.com/@{username}'
    
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.1.9 Chrome/83.0.4103.122 Electron/9.4.4 Safari/537.36',
        'accept-language': 'en-GB'
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    with open('tiktok2.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
    
    script = soup.find('script', {'id': '__UNIVERSAL_DATA_FOR_REHYDRATION__'})
    data:dict = json.loads(script.text)['__DEFAULT_SCOPE__']['webapp.user-detail']
    
    return data.get('userInfo')


def main():
    username = input(fade.water("Enter the TikTok username: ")).strip()
    print()
    
    if not username:
        Slow(fade.water("Username cannot be empty."))
        return
    
    data = get_tiktok_user_info(username)
    
    if data is None:
        Slow(fade.water(f"Error: No user found with the username '{username}'."))
    else:
        user_data:dict = data.get('user', {})
        stats:dict = data.get('stats', {})
        
        Slow(fade.water("TikTok User Information:"))
        Slow(fade.water(f"Username: {user_data.get('uniqueId')}"))
        Slow(fade.water(f'Nickname: {user_data.get("nickname")}'))
        Slow(fade.water(f'User ID: {user_data.get("id")}'))
        Slow(fade.water(f'Description: {user_data.get("signature")}'))
        Slow(fade.water(f'Creation Date: {datetime.fromtimestamp(user_data.get("createTime")).strftime("%d-%m-%Y at %H:%M:%S")}'))
        Slow(fade.water(f'Region: {user_data.get("region")}'))
        Slow(fade.water(f'Language: {user_data.get("language")}'))
        Slow(fade.water(f'Friends: {stats.get("friendCount"):,}'))
        Slow(fade.water(f'Followers: {stats.get("followerCount"):,}'))
        Slow(fade.water(f'Following: {stats.get("followingCount"):,}'))
        Slow(fade.water(f'Hearts: {stats.get("heartCount"):,}'))
        Slow(fade.water(f'Videos: {stats.get("videoCount"):,}'))
        Slow(fade.water(f'Verified: {user_data.get("verified")}'))
        Slow(fade.water(f'Private Account: {user_data.get("secret")}'))
        Slow(fade.water(f'Open favorite: {user_data.get("openFavorite")}'))




if __name__ == "__main__":
    main()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
