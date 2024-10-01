import os
import webbrowser
import time
import fade

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)
    print()

def show_intro():
    intro = """
 ▒█████    ██████  ██▓ ███▄    █ ▄▄▄█████▓    ███▄    █  ▄▄▄    ██▒   █▓ ██▓  ▄████  ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
▒██▒  ██▒▒██    ▒ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒    ██ ▀█   █ ▒████▄ ▓██░   █▒▓██▒ ██▒ ▀█▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▒██░  ██▒░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░   ▓██  ▀█ ██▒▒██  ▀█▄▓██  █▒░▒██▒▒██░▄▄▄░▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
▒██   ██░  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░    ▓██▒  ▐▌██▒░██▄▄▄▄██▒██ █░░░██░░▓█  ██▓░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
░ ████▓▒░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░    ▒██░   ▓██░ ▓█   ▓██▒▒▀█░  ░██░░▒▓███▀▒ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░      ░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▐░  ░▓   ░▒   ▒  ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
  ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░       ░ ░░   ░ ▒░  ▒   ▒▒ ░░ ░░   ▒ ░  ░   ░   ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
░ ░ ░ ▒  ░  ░  ░   ▒ ░   ░   ░ ░   ░            ░   ░ ░   ░   ▒     ░░   ▒ ░░ ░   ░   ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
    ░ ░        ░   ░           ░                      ░       ░  ░   ░   ░        ░       ░  ░            ░ ░     ░     
                                                                    ░                                                   

                - Appuyer Enter
    """
    Slow(fade.water(intro))
    input()

def print_banner():
    clear_screen()
    banner = """
 ▒█████    ██████  ██▓ ███▄    █ ▄▄▄█████▓    ███▄    █  ▄▄▄    ██▒   █▓ ██▓  ▄████  ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
▒██▒  ██▒▒██    ▒ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒    ██ ▀█   █ ▒████▄ ▓██░   █▒▓██▒ ██▒ ▀█▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▒██░  ██▒░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░   ▓██  ▀█ ██▒▒██  ▀█▄▓██  █▒░▒██▒▒██░▄▄▄░▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
▒██   ██░  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░    ▓██▒  ▐▌██▒░██▄▄▄▄██▒██ █░░░██░░▓█  ██▓░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
░ ████▓▒░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░    ▒██░   ▓██░ ▓█   ▓██▒▒▀█░  ░██░░▒▓███▀▒ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░      ░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▐░  ░▓   ░▒   ▒  ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
  ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░       ░ ░░   ░ ▒░  ▒   ▒▒ ░░ ░░   ▒ ░  ░   ░   ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
░ ░ ░ ▒  ░  ░  ░   ▒ ░   ░   ░ ░   ░            ░   ░ ░   ░   ▒     ░░   ▒ ░░ ░   ░   ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
    ░ ░        ░   ░           ░                      ░       ░  ░   ░   ░        ░       ░  ░            ░ ░     ░     
                                                                    ░                                                   
    """
    Slow(fade.water(banner))

def show_main_menu():
    print_banner()
    menu = "[01] -> IP                      [02] -> Email                [03] -> Nom prénoms          [04] -> Visage                [05] -> Quitter"
    Slow(fade.water(menu))
    option = input(fade.water("\nChoisissez une option : "))
    return option

def ip_menu():
    while True:
        print_banner()
        menu = "[01] -> Snusbase                [02] -> Intelx               [03] -> Shodan               [04] -> Retour au menu"
        Slow(fade.water(menu))
        ip_option = input(fade.water("\nChoisissez une option : "))
        if ip_option == "1":
            webbrowser.open("https://snusbase.com/")
        elif ip_option == "2":
            webbrowser.open("https://intelx.io/")
        elif ip_option == "3":
            webbrowser.open("https://www.shodan.io")
        elif ip_option == "4":
            break
        else:
            Slow(fade.water("Option invalide, veuillez réessayer."))
        input(fade.water("\nAppuyez sur Entrée pour continuer..."))

def email_menu():
    while True:
        print_banner()
        menu = "[01] -> Hunter                  [02] -> HaveIBeenPwned       [03] -> Emailrep             [04] -> Epieos                [05] -> Snusbase             [06] -> Retour au menu"
        Slow(fade.water(menu))
        email_option = input(fade.water("\nChoisissez une option : "))
        if email_option == "1":
            webbrowser.open("https://hunter.io")
        elif email_option == "2":
            webbrowser.open("https://haveibeenpwned.com")
        elif email_option == "3":
            webbrowser.open("https://emailrep.io/")
        elif email_option == "4":
            webbrowser.open("https://epieos.com/")
        elif email_option == "5":
            webbrowser.open("https://snusbase.com/")
        elif email_option == "6":
            break
        else:
            Slow(fade.water("Option invalide, veuillez réessayer."))
        input(fade.water("\nAppuyez sur Entrée pour continuer..."))

def main():
    clear_screen()
    show_intro()
    while True:
        option = show_main_menu()
        if option == "1":
            ip_menu()
        elif option == "2":
            email_menu()
        elif option == "3":
            webbrowser.open("https://some-names-database-url.com/")
        elif option == "4":
            webbrowser.open("https://some-faces-database-url.com/")
        elif option == "5":
            time.sleep(2)
            os.system("python ../../main.py")
            break
        else:
            Slow(fade.water("Option invalide, veuillez réessayer."))
        input(fade.water("\nAppuyez sur Entrée pour continuer..."))

if __name__ == "__main__":
    main()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
