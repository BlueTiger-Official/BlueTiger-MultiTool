import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from pystyle import Colorate, Colors
import time
import os

def Slow(texte):
    for line in texte.splitlines():
        print(line)
        time.sleep(0.05)

def display_ascii_art():
    ascii_art = """
 ██▓███   ██░ ██  ▒█████   ███▄    █ ▓█████     ██▓ ███▄    █   █████▒▒█████  
▓██░  ██▒▓██░ ██▒▒██▒  ██▒ ██ ▀█   █ ▓█   ▀    ▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒
▓██░ ██▓▒▒██▀▀██░▒██░  ██▒▓██  ▀█ ██▒▒███      ▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒
▒██▄█▓▒ ▒░▓█ ░██ ▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄    ░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░
▒██▒ ░  ░░▓█▒░██▓░ ████▓▒░▒██░   ▓██░░▒████▒   ░██░▒██░   ▓██░░▒█░   ░ ████▓▒░
▒▓▒░ ░  ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░   ░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░ 
░▒ ░      ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░    ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░ 
░░        ░  ░░ ░░ ░ ░ ▒     ░   ░ ░    ░       ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒  
          ░  ░  ░    ░ ░           ░    ░  ░    ░           ░            ░ ░  
                                                                                 
                                                              
    """
    colored_ascii_art = Colorate.Horizontal(Colors.blue_to_red, ascii_art)
    Slow(colored_ascii_art)

def get_phone_info(phone_number):
    Slow(Colorate.Horizontal(Colors.blue_to_red, "Information Recovery..."))
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        if phonenumbers.is_valid_number(parsed_number):
            if phone_number.startswith("+"):
                country_code = "+" + phone_number[1:3]
            else:
                country_code = "None"
            operator = carrier.name_for_number(parsed_number, "fr")
            type_number = "Mobile" if phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE else "Fixe"
            timezones = timezone.time_zones_for_number(parsed_number)
            timezone_info = timezones[0] if timezones else "None"
            country = phonenumbers.region_code_for_number(parsed_number)
            region = geocoder.description_for_number(parsed_number, "fr")
            status = "Valid"

            Slow(Colorate.Horizontal(Colors.blue_to_red, f"""
Phone        : {phone_number}
Country Code : {country_code}
Country      : {country}
Region       : {region}
Timezone     : {timezone_info}
Operator     : {operator}
Type Number  : {type_number}
                
            """))
        else:
            Slow(Colorate.Horizontal(Colors.blue_to_red, "Invalid Format ! [Ex: +442012345678 or +33623456789]"))

    except Exception as e:
        Slow(Colorate.Horizontal(Colors.blue_to_red, f"Exception occurred: {e}"))

def menu():
    display_ascii_art()

    try:
        while True:
            phone_number = input(Colorate.Horizontal(Colors.blue_to_red, "\nPhone Number -> "))
            get_phone_info(phone_number)

            choice = input(Colorate.Horizontal(Colors.blue_to_red,"Do you want to continue? (y/n): ").strip().lower())
            if choice != 'y':
                break

    except Exception as e:
        Slow(Colorate.Horizontal(Colors.blue_to_red, f"Error: {e}"))

if __name__ == "__main__":
    menu()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')