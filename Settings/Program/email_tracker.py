import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
import fade
import os

def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)
    print()

class EmailTracker:
    def __init__(self, email):
        self.email = email
        self.session = requests.Session()
        self.ua = UserAgent()

        self.sites = [
            self.Instagram,
            self.Twitter,
            self.Pinterest,
            self.Imgur,
            self.Patreon,
            self.Spotify,
            self.FireFox,
            self.LastPass,
            self.Archive,
            self.PornHub,
            self.Xnxx,
            self.Xvideo
        ]

    def track_emails(self):
        results = []
        for site in self.sites:
            result = site(self.email)
            results.append((site.__name__, result))
        return results
    
    def Instagram(self, email):
        try:
            session = requests.Session()
            user_agent = self.ua.random
            headers = {
                'User-Agent': user_agent,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Origin': 'https://www.instagram.com',
                'Connection': 'keep-alive',
                'Referer': 'https://www.instagram.com/'
            }

            data = {"email": email}
            response = session.get(
                "https://www.instagram.com/accounts/emailsignup/", 
                headers=headers
            )
            if response.status_code == 200:
                if 'csrftoken' in session.cookies:
                    token = session.cookies['csrftoken']
                else:
                    return "Error: Token Not Found."

                headers["x-csrftoken"] = token
                headers["Referer"] = "https://www.instagram.com/accounts/emailsignup/"
                response = session.post(
                    url="https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/",
                    headers=headers,
                    data=data
                )
                if response.status_code == 200:
                    if "Another account is using the same email." in response.text or "email_is_taken" in response.text:
                        return True
                    else:
                        return False
                else:
                    return f"Error: {response.status_code}"
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return f"Error: {e}"

    def Twitter(self, email):
        try:
            session = requests.Session()
            user_agent = self.ua.random
            headers = {'User-Agent': user_agent}

            response = session.get(
                url="https://api.twitter.com/i/users/email_available.json",
                params={"email": email}
            )
            if response.status_code == 200:
                return response.json().get("taken", False)
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return f"Error: {e}"

    def Pinterest(self, email):
        try:
            session = requests.Session()
            user_agent = self.ua.random
            headers = {'User-Agent': user_agent}

            response = session.get(
                "https://www.pinterest.com/_ngjs/resource/EmailExistsResource/get/",
                params={"source_url": "/", "data": '{"options": {"email": "' + email + '"}, "context": {}}'},
                headers=headers
            )
            if response.status_code == 200:
                message = response.json().get("resource_response", {}).get("message", "")
                if message == "Invalid email.":
                    return False
                elif message == "ok":
                    return response.json().get("resource_response", {}).get("data", False)
                else:
                    return False
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return f"Error: {e}"

    def Imgur(self, email):
        try:
            session = requests.Session()
            user_agent = self.ua.random
            headers = {
                'User-Agent': user_agent,
                'Accept': '*/*',
                'Accept-Language': 'en,en-US;q=0.5',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://imgur.com',
                'DNT': '1',
                'Connection': 'keep-alive',
                'TE': 'Trailers',
            }

            session.get("https://imgur.com/register?redirect=%2Fuser", headers=headers)

            headers["X-Requested-With"] = "XMLHttpRequest"
            data = {'email': email}
            response = session.post('https://imgur.com/signin/ajax_email_available', headers=headers, data=data)

            if response.status_code == 200:
                available = response.json().get('data', {}).get("available", False)
                if available:
                    return False
                elif "Invalid email domain" in response.text:
                    return False
                else:
                    return True
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return f"Error: {e}"

    def Patreon(self, email):
        try:
            session = requests.Session()
            user_agent = self.ua.random
            headers = {
                'User-Agent': user_agent,
                'Accept': '*/*',
                'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'X-Requested-With': 'XMLHttpRequest',
                'Origin': 'https://www.plurk.com',
                'DNT': '1',
                'Connection': 'keep-alive',
            }
            data = {'email': email}
            response = session.post('https://www.plurk.com/Users/isEmailFound', headers=headers, data=data)
            if response.status_code == 200:
                if "True" in response.text:
                    return True
                elif "False" in response.text:
                    return False
                else:
                    return False
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return f"Error: {e}"
        
    def Spotify(self, email):
        try:
            session = requests.Session()
            user_agent = self.ua.random
            headers = {
                'User-Agent': user_agent,
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'en-US,en;q=0.5',
                'DNT': '1',
                'Connection': 'keep-alive',
            }
            params = {'validate': '1', 'email': email}
            response = session.get('https://spclient.wg.spotify.com/signup/public/v1/account',
                    headers=headers,
                    params=params)
            if response.status_code == 200:
                status = response.json().get("status", 0)
                return status == 20
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return f"Error: {e}"

    def FireFox(self, email):
        try:
            session = requests.Session()
            data = {"email": email}
            response = session.post(
                "https://api.accounts.firefox.com/v1/account/status",
                data=data
            )
            if response.status_code == 200:
                return "true" in response.text
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return f"Error: {e}"

    def LastPass(self, email):
        try:
            session = requests.Session()
            user_agent = self.ua.random
            headers = {
                'User-Agent': user_agent,
                'Accept': '*/*',
                'Accept-Language': 'en,en-US;q=0.5',
                'Referer': 'https://lastpass.com/',
                'X-Requested-With': 'XMLHttpRequest',
                'DNT': '1',
                'Connection': 'keep-alive',
                'TE': 'Trailers',
            }
            params = {
                'check': 'avail',
                'skipcontent': '1',
                'mistype': '1',
                'username': email,
            }
            response = session.get(
                f'https://lastpass.com/create_account.php?check=avail&skipcontent=1&mistype=1&username={str(email).replace("@", "%40")}',       
                params=params,
                headers=headers)
            if response.status_code == 200:
                if "no" in response.text:
                    return True
                elif "emailinvalid" in response.text or "ok" in response.text:
                    return False
                else:
                    return False
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return f"Error: {e}"
        
    def Archive(self, email):
        try:
            session = requests.Session()
            user_agent = self.ua.random
            headers = {
                'User-Agent': user_agent,
                'Accept': '*/*',
                'Accept-Language': 'en,en-US;q=0.5',
                'X-Requested-With': 'XMLHttpRequest',
                'DNT': '1',
                'Connection': 'keep-alive',
                'TE': 'Trailers',
            }
            params = {'email': email}
            response = session.get(
                'https://web.archive.org/cdx/search/cdx?url=*&filter=url:*'+email+'*',
                headers=headers,
                params=params
            )
            if response.status_code == 200:
                return response.text
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return f"Error: {e}"

    def PornHub(self, email):
        try:
            session = requests.Session()
            user_agent = self.ua.random
            headers = {'User-Agent': user_agent}
            data = {'email': email}
            response = session.post(
                'https://www.pornhub.com/users/ajax/check_email',
                headers=headers,
                data=data
            )
            if response.status_code == 200:
                if "exists" in response.json().get("status", ""):
                    return True
                else:
                    return False
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return f"Error: {e}"
        
    def Xnxx(self, email):
        try:
            session = requests.Session()
            user_agent = self.ua.random
            headers = {'User-Agent': user_agent}
            data = {'email': email}
            response = session.post(
                'https://www.xnxx.com/users/ajax/check_email',
                headers=headers,
                data=data
            )
            if response.status_code == 200:
                if "exists" in response.json().get("status", ""):
                    return True
                else:
                    return False
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return f"Error: {e}"

    def Xvideo(self, email):
        try:
            session = requests.Session()
            user_agent = self.ua.random
            headers = {'User-Agent': user_agent}
            data = {'email': email}
            response = session.post(
                'https://www.xvideo.com/users/ajax/check_email',
                headers=headers,
                data=data
            )
            if response.status_code == 200:
                if "exists" in response.json().get("status", ""):
                    return True
                else:
                    return False
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return f"Error: {e}"

if __name__ == "__main__":
    Slow("Email Tracker")
    email = input(fade.water("Enter the email address to check: "))
    tracker = EmailTracker(email)
    results = tracker.track_emails()

    for site, result in results:
        Slow(f"{site}: {'Taken' if result else 'Available' if result is not False else result}")    
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
