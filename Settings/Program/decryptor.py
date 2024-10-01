import bcrypt
import hashlib
import base64
import fade
import os
import time

banner = """
▓█████▄ ▓█████  ▄████▄   ██▀███ ▓██   ██▓ ██▓███  ▄▄▄█████▓ ▒█████   ██▀███  
▒██▀ ██▌▓█   ▀ ▒██▀ ▀█  ▓██ ▒ ██▒▒██  ██▒▓██░  ██▒▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
░██   █▌▒███   ▒▓█    ▄ ▓██ ░▄█ ▒ ▒██ ██░▓██░ ██▓▒▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
░▓█▄   ▌▒▓█  ▄ ▒▓▓▄ ▄██▒▒██▀▀█▄   ░ ▐██▓░▒██▄█▓▒ ▒░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
░▒████▓ ░▒████▒▒ ▓███▀ ░░██▓ ▒██▒ ░ ██▒▓░▒██▒ ░  ░  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
 ▒▒▓  ▒ ░░ ▒░ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░  ██▒▒▒ ▒▓▒░ ░  ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
 ░ ▒  ▒  ░ ░  ░  ░  ▒     ░▒ ░ ▒░▓██ ░▒░ ░▒ ░         ░      ░ ▒ ▒░   ░▒ ░ ▒░
 ░ ░  ░    ░   ░          ░░   ░ ▒ ▒ ░░  ░░         ░      ░ ░ ░ ▒    ░░   ░ 
   ░       ░  ░░ ░         ░     ░ ░                           ░ ░     ░     
 ░             ░                 ░ ░                                                                       
"""

def Slow(texte):
    for line in texte.splitlines():
        print(line)
        time.sleep(0.05)

def display_with_banner():
    print(fade.water(banner))

def md5_verify(text, hashed):
    return hashlib.md5(text.encode()).hexdigest() == hashed

def sha1_verify(text, hashed):
    return hashlib.sha1(text.encode()).hexdigest() == hashed

def sha256_verify(text, hashed):
    return hashlib.sha256(text.encode()).hexdigest() == hashed

def pbkdf2_verify(text, hashed):
    dk, salt = base64.b64decode(hashed).split(b'|')
    return hashlib.pbkdf2_hmac('sha256', text.encode(), salt, 100000) == dk

def base64_decode(encoded):
    return base64.b64decode(encoded).decode()

def main():
    while True:
        display_with_banner()

        menu = fade.water("""
╔═════════════════════════════════════════════════╗
║              Decryptor                          ║
╠═════════════════════════════════════════════════╣
║  01. BCRYPT                                     ║
║  02. MD5                                        ║
║  03. SHA-1                                      ║
║  04. SHA-256                                    ║
║  05. PBKDF2 (SHA-256)                           ║
║  06. Base64                                     ║
╚═════════════════════════════════════════════════╝
        """)

        Slow(menu)
        choice = input(fade.water("Votre choix: ")).strip()

        if choice not in ['01', '02', '03', '04', '05', '06']:
            print(fade.water("Choix invalide. Veuillez réessayer."))
            continue

        text = input(fade.water("Entrez le texte à vérifier/décrypter: ")).strip()

        try:
            if choice == '01':
                hashed = input(fade.water("Entrez le hash BCRYPT: ")).strip()
                result = bcrypt.checkpw(text.encode(), hashed.encode())
            elif choice == '02':
                hashed = input(fade.water("Entrez le hash MD5: ")).strip()
                result = md5_verify(text, hashed)
            elif choice == '03':
                hashed = input(fade.water("Entrez le hash SHA-1: ")).strip()
                result = sha1_verify(text, hashed)
            elif choice == '04':
                hashed = input(fade.water("Entrez le hash SHA-256: ")).strip()
                result = sha256_verify(text, hashed)
            elif choice == '05':
                hashed = input(fade.water("Entrez le hash PBKDF2 (SHA-256): ")).strip()
                result = pbkdf2_verify(text, hashed)
            elif choice == '06':
                decoded = base64_decode(text)
                print(fade.water(f"Base64 décodé: {decoded}"))
                continue

            if result:
                print(fade.water("Le texte correspond au hash!"))
            else:
                print(fade.water("Le texte ne correspond pas au hash!"))
        except Exception as e:
            print(fade.water(f"Une erreur s'est produite : {e}"))

        if input(fade.water("Voulez-vous vérifier un autre texte? (oui/non): ")).strip().lower() != 'oui':
            break

    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.chdir("../../")
    import os    
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')

if __name__ == "__main__":
    main()
