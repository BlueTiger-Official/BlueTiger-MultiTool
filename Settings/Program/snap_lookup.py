import requests
from bs4 import BeautifulSoup
import fade
import os
import time

def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)
    print()

def display_welcome_message():
    ascii_art = """
  ██████  ███▄    █  ▄▄▄       ██▓███      ██▓     ▒█████   ▒█████   ██ ▄█▀ █    ██  ██▓███  
▒██    ▒  ██ ▀█   █ ▒████▄    ▓██░  ██▒   ▓██▒    ▒██▒  ██▒▒██▒  ██▒ ██▄█▒  ██  ▓██▒▓██░  ██▒
░ ▓██▄   ▓██  ▀█ ██▒▒██  ▀█▄  ▓██░ ██▓▒   ▒██░    ▒██░  ██▒▒██░  ██▒▓███▄░ ▓██  ▒██░▓██░ ██▓▒
  ▒   ██▒▓██▒  ▐▌██▒░██▄▄▄▄██ ▒██▄█▓▒ ▒   ▒██░    ▒██   ██░▒██   ██░▓██ █▄ ▓▓█  ░██░▒██▄█▓▒ ▒
▒██████▒▒▒██░   ▓██░ ▓█   ▓██▒▒██▒ ░  ░   ░██████▒░ ████▓▒░░ ████▓▒░▒██▒ █▄▒▒█████▓ ▒██▒ ░  ░
▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒  ▒▒   ▓▒█░▒▓▒░ ░  ░   ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
░ ░▒  ░ ░░ ░░   ░ ▒░  ▒   ▒▒ ░░▒ ░        ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░░░▒░ ░ ░ ░▒ ░     
░  ░  ░     ░   ░ ░   ░   ▒   ░░            ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░  ░░░ ░ ░ ░░       
      ░           ░       ░  ░                ░  ░    ░ ░      ░ ░  ░  ░      ░              
                                                                                             
    """
    ascii_fade = fade.water(ascii_art)
    Slow(ascii_art)
    print()

def scrape_snapchat_user(username):
    url = f"https://story.snapchat.com/u/{username}"
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        
        user_info = {}
        
        display_name = soup.find('meta', property='og:title')
        if display_name:
            user_info['Display Name'] = display_name.get('content', 'Not available')
        
        description = soup.find('meta', property='og:description')
        if description:
            user_info['Description'] = description.get('content', 'Not available')
        
        profile_image = soup.find('meta', property='og:image')
        if profile_image:
            user_info['Profile Image URL'] = profile_image.get('content', 'Not available')
        
        stories = soup.find_all('div', class_='sc-fzXfMT')
        if stories:
            user_info['Stories'] = [story.get('data-story', 'Not available') for story in stories]
        
        links = soup.find_all('a')
        if links:
            user_info['Links'] = [link.get('href', 'Not available') for link in links]
        
        location_tag = soup.find('meta', property='og:locality')
        if location_tag:
            user_info['Location'] = location_tag.get('content', 'Not available')
        else:
            if description and 'à' in description.get('content', ''):
                location_start = description['content'].find('à')
                location = description['content'][location_start+2:].split()[0]
                user_info['Location'] = location

        og_meta = soup.find_all('meta', property=lambda x: x and x.startswith('og:'))
        for meta in og_meta:
            property_name = meta.get('property')
            content = meta.get('content')
            if property_name and content:
                user_info[property_name] = content

        return user_info if user_info else {'Error': 'No information found for this user.'}

    except requests.exceptions.HTTPError as http_err:
        Slow(fade.water(f"HTTP error occurred: {http_err}"))
    except Exception as err:
        Slow(fade.water(f"Other error occurred: {err}"))
    return {'Error': 'Failed to retrieve information'}

def main():
    display_welcome_message()
    username = input(fade.water("Enter Snapchat username: "))
    user_info = scrape_snapchat_user(username)

    if user_info:
        Slow(fade.water("\nUser Information:"))
        for key, value in user_info.items():
            Slow(fade.water(f"{key}: {value}"))
    else:
        Slow(fade.water("No information found for this user."))

if __name__ == "__main__":
    main()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')