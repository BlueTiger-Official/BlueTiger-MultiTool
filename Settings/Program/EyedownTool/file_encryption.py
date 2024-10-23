import os
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)
    print(f"[+] Fichier chiffré : {file_path}")

def encrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

def display_menu():
    print("\n=== Menu de Chiffrement ===")
    print("1. Chiffrer un fichier")
    print("2. Chiffrer un dossier")
    print("3. Générer une clé de chiffrement")
    print("4. Quitter")

def main():
    while True:
        display_menu()
        action = input("Sélectionnez une option (1/2/3/4) : ")

        if action == "1":
            file_path = input("Entrez le chemin du fichier à chiffrer : ")
            if os.path.isfile(file_path):
                key = generate_key() if not os.path.exists("secret.key") else load_key()
                encrypt_file(file_path, key)
            else:
                print("[-] Le chemin spécifié n'est pas un fichier.")
        
        elif action == "2":
            folder_path = input("Entrez le chemin du dossier à chiffrer : ")
            if os.path.isdir(folder_path):
                key = generate_key() if not os.path.exists("secret.key") else load_key()
                encrypt_folder(folder_path, key)
            else:
                print("[-] Le chemin spécifié n'est pas un dossier.")
        
        elif action == "3":
            if os.path.exists("secret.key"):
                print("[+] Clé de chiffrement existante déjà créée.")
            else:
                generate_key()
                print("[+] Clé de chiffrement générée : secret.key")
        
        elif action == "4":
            print("[*] Processus annulé par l'utilisateur.")
            break
        
        else:
            print("[-] Action non reconnue. Veuillez choisir 1, 2, 3 ou 4.")

if __name__ == "__main__":
    main()
