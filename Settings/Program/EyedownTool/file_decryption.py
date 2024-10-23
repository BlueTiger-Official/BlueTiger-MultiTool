import os
from cryptography.fernet import Fernet

def load_key():
    return open("secret.key", "rb").read()

def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)
    print(f"[+] Fichier déchiffré : {file_path}")

def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)

def display_menu():
    print("\n=== Menu de Déchiffrement ===")
    print("1. Déchiffrer un fichier")
    print("2. Déchiffrer un dossier")
    print("3. Quitter")

def main():
    key = load_key()

    while True:
        display_menu()
        action = input("Sélectionnez une option (1/2/3) : ")

        if action == "1":
            file_path = input("Entrez le chemin du fichier à déchiffrer : ")
            if os.path.isfile(file_path):
                decrypt_file(file_path, key)
            else:
                print("[-] Le chemin spécifié n'est pas un fichier.")
        
        elif action == "2":
            folder_path = input("Entrez le chemin du dossier à déchiffrer : ")
            if os.path.isdir(folder_path):
                decrypt_folder(folder_path, key)
            else:
                print("[-] Le chemin spécifié n'est pas un dossier.")
        
        elif action == "3":
            print("[*] Processus annulé par l'utilisateur.")
            break
        
        else:
            print("[-] Action non reconnue. Veuillez choisir 1, 2 ou 3.")

if __name__ == "__main__":
    main()
