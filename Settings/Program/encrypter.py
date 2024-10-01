import bcrypt
import hashlib
import base64
import fade
import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)
    print()

def display_with_ascii_art(content):
    clear_console()
    Slow(fade.water("""
▓█████  ███▄    █  ▄████▄   ██▀███ ▓██   ██▓ ██▓███  ▄▄▄█████▓▓█████  ██▀███  
▓█   ▀  ██ ▀█   █ ▒██▀ ▀█  ▓██ ▒ ██▒▒██  ██▒▓██░  ██▒▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
▒███   ▓██  ▀█ ██▒▒▓█    ▄ ▓██ ░▄█ ▒ ▒██ ██░▓██░ ██▓▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
▒▓█  ▄ ▓██▒  ▐▌██▒▒▓▓▄ ▄██▒▒██▀▀█▄   ░ ▐██▓░▒██▄█▓▒ ▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  
░▒████▒▒██░   ▓██░▒ ▓███▀ ░░██▓ ▒██▒ ░ ██▒▓░▒██▒ ░  ░  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
░░ ▒░ ░░ ▒░   ▒ ▒ ░ ░▒ ▒  ░░ ▒▓ ░▒▓░  ██▒▒▒ ▒▓▒░ ░  ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
 ░ ░  ░░ ░░   ░ ▒░  ░  ▒     ░▒ ░ ▒░▓██ ░▒░ ░▒ ░         ░     ░ ░  ░  ░▒ ░ ▒░
   ░      ░   ░ ░ ░          ░░   ░ ▒ ▒ ░░  ░░         ░         ░     ░░   ░ 
   ░  ░         ░ ░ ░         ░     ░ ░                          ░  ░   ░     
                  ░                 ░ ░                                       
"""))
    Slow(content)

def bcrypt_encrypt(text):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(text.encode(), salt)
    return hashed.decode()

def md5_encrypt(text):
    return hashlib.md5(text.encode()).hexdigest()

def sha1_encrypt(text):
    return hashlib.sha1(text.encode()).hexdigest()

def sha256_encrypt(text):
    return hashlib.sha256(text.encode()).hexdigest()

def pbkdf2_encrypt(text):
    salt = os.urandom(16)
    hashed = hashlib.pbkdf2_hmac('sha256', text.encode(), salt, 100000)
    return base64.b64encode(salt + hashed).decode()

def base64_encode(text):
    return base64.b64encode(text.encode()).decode()

def main():
    while True:
        try:
            display_with_ascii_art(
                "Choisissez l'algorithme d'encryptage:\n[01] -> BCRYPT\n[02] -> MD5\n[03] -> SHA-1\n[04] -> SHA-256\n[05] -> PBKDF2 (SHA-256)\n[06] -> Base64 Encode")
            choice = input("Entrez le numéro de votre choix: ").strip()
            text = input("Entrez le texte à encrypter: ").strip()

            if choice == '01':
                result = bcrypt_encrypt(text)
            elif choice == '02':
                result = md5_encrypt(text)
            elif choice == '03':
                result = sha1_encrypt(text)
            elif choice == '04':
                result = sha256_encrypt(text)
            elif choice == '05':
                result = pbkdf2_encrypt(text)
            elif choice == '06':
                result = base64_encode(text)
            else:
                display_with_ascii_art("Choix invalide. Veuillez réessayer.")
                continue

            display_with_ascii_art(f"Résultat de l'encryption: {result}")
            input("\nAppuyez sur Entrée pour continuer...")

            display_with_ascii_art("Voulez-vous effectuer une autre encryption? (oui/non)")
            again = input().strip().lower()
            if again != 'oui':
                break

        except Exception as e:
            display_with_ascii_art(f"Une erreur est survenue: {str(e)}")
            input("\nAppuyez sur Entrée pour continuer...")



if __name__ == "__main__":
    main()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
