import fade
import subprocess
import os

options = {
    '01': {"name": "Boost-Tool (Dsc) (UPDATE)", "script": "boost_tool.py"},
    '02': {"name": "Cleaner (Token,etc)", "script": "cleaner.py"},
    '03': {"name": "Discord-Bot-Client", "script": "discord_bot_client.py"},
    '04': {"name": "Fake-Decoration (Dsc)", "script": "fake_decoration.py"},
    '05': {"name": "Login-Token (Web)", "script": "login_token_extensions.py"},
    '06': {"name": "Mass-Report (Dsc)", "script": "massreport_discord.py"},
    '07': {"name": "Nitro-Gen (Dsc)", "script": "nitro.py"},
    '08': {"name": "Raid-Menu (Dsc)", "script": "raid_menu.py"},
    '09': {"name": "Username-Tracker", "script": "username_tracker.py"},
    '10': {"name": "Email-Tracker", "script": "email_tracker.py"},
    '11': {"name": "Email-Lookup", "script": "email_lookup.py"},
    '12': {"name": "Phone-Number-Lookup", "script": "phone_number_lookup.py"},
    '13': {"name": "Ip-Lookup", "script": "ip_lookup.py"},
    '14': {"name": "Search-In-DataBase", "script": "search_in_database.py"},
    '15': {"name": "Dark-Web-Links", "script": "dark_web_links.py"},
    '16': {"name": "Dumper Fivem", "script": "dumper.py"},
    '17': {"name": "Searcher-DB", "script": "search_db.py"},
    '18': {"name": "Searcher-DB-API-NKRZ", "script": "search_db_api_nkrz.py"},
    '19': {"name": "Instagram-Lookup", "script": "search_insta.py"},
    '20': {"name": "Name-Lookup", "script": "search_name.py"},
    '21': {"name": "Snapchat-Lookup", "script": "snap_lookup.py"},
    '22': {"name": "Website-Info", "script": "website_info.py"},
    '23': {"name": "Tiktok-Lookup", "script": "tiktok_lookup.py"},
    '24': {"name": "Steam-Lookup", "script": "steam_lookup.py"},
    '25': {"name": "SQL-Vulnérability-Scanner", "script": "sql_vuln.py"},
    '26': {"name": "XSS-Vulnérability-Scanner", "script": "xss_vuln.py"},
    '27': {"name": "Tiktok-Tool (Paid)", "script": "tiktok.py"},
    '28': {"name": "Rat-Discord (Paid)", "script": "rat_discord.py"},
    '29': {"name": "Ebook (Paid)", "script": "ebook.py"},
    '30': {"name": "Database (Paid)", "script": "db.py"},
    '31': {"name": "Brute-DD0S", "script": "brute_ddos.py"},
    '32': {"name": "Server-Fivem-Lookup", "script": "cfxinfo_lookup.py"},
    '33': {"name": "Statuts Rotator", "script": "status_rotator.py"},
    '34': {"name": "Check-Username", "script": "check_username.py"},
    '35': {"name": "Dark-Gpt", "script": "darkgpt.py"},
    '36': {"name": "Database-Leak-Dl", "script": "db_dl.py"},
    '37': {"name": "Decryptor", "script": "decryptor.py"},
    '38': {"name": "Email-Bomber", "script": "email_bomber.py"},
    '39': {"name": "Email-Info", "script": "email_info.py"},
    '40': {"name": "Encrypter", "script": "encrypter.py"},
    '41': {"name": "Ip-Tv", "script": "ip_tv.py"},
    '42': {"name": "Number-Info", "script": "number_info.py"},
    '43': {"name": "Onion-Link", "script": "onion_links.py"},
    '44': {"name": "Osint-Navigator", "script": "osint_navigator.py"},
    '45': {"name": "Port-Checker", "script": "portcheck.py"},
    '46': {"name": "Proxy-Scrapper", "script": "proxy_scrapper.py"},
    '47': {"name": "IP-Scanner", "script": "scanner.py"},
    '48': {"name": "Scrap-CFX-ID", "script": "scrapid.py"},
    '49': {"name": "SnusBase-Cookies", "script": "snus_cookies.py"},
    '50': {"name": "SnusBase", "script": "snusbase.py"},
    '51': {"name": "Spotify-No-Pub", "script": "spotify_no_pub.py"},
    '52': {"name": "Token Checker", "script": "token_checker.py"},
    '53': {"name": "Token Info", "script": "token_info.py"},
    '54': {"name": "Webhook Info", "script": "webhook_info.py"},
    '55': {"name": "Webhook Menu", "script": "webhook_menu.py"},
    '56': {"name": "TikTok", "script": "tiktok_brute.py"},
    '57': {"name": "Instagram", "script": "instagram.py"},
    '58': {"name": "SnapChat", "script": "snapchat.py"},
    '59': {"name": "Spoofer", "script": "spoofer.py"},
    '60': {"name": "Spoofer", "script": "spoof_tkinter.py"}
    
}





def format_option(option_key, width=21):
    option = options.get(option_key, {"name": "Unknown Option"})
    return option['name'].replace('-', ' ').ljust(width)

def format_navigation_option(text, width=17):
    return text.ljust(width)



def StartProgram(script_name):
    try:
        script_path = os.path.join('Settings', 'Program', script_name)
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de {script_name}: {e}")
    except FileNotFoundError:
        print(f"Le fichier {script_name} n'a pas été trouvé dans 'Settings/Program/'.")

option_back = "Back"
option_next = "Next"
option_site = "Site"
option_info = "Info"

option_back_txt = fade.blackwhite(format_navigation_option(f"{option_back} [B]"))
option_next_txt = fade.blackwhite(format_navigation_option(f"{option_next} [N]"))
option_site_txt = fade.blackwhite(format_navigation_option(f"[S] {option_site}"))
option_info_txt = fade.blackwhite(format_navigation_option(f"[I] {option_info}"))
