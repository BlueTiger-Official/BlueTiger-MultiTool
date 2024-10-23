import os
import platform

def unblock_all_sites():
    if platform.system() == "Windows":
        hosts_file = r"C:\Windows\System32\drivers\etc\hosts"
    else:
        hosts_file = "/etc/hosts"

    try:
        with open(hosts_file, 'w') as file:
            file.write("") 
            
        print("[+] Tous les sites ont été débloqués avec succès.")
    except PermissionError:
        print("[-] Échec : veuillez exécuter ce script avec des privilèges d'administrateur.")
    except Exception as e:
        print(f"[-] Une erreur s'est produite : {str(e)}")

def main_menu():
    while True:
        print("\n[*] Menu Principal")
        print("1. Débloquer tous les sites")
        print("0. Quitter")

        choice = input("Sélectionnez une option : ")

        if choice == '1':
            unblock_all_sites()
        elif choice == '0':
            print("[-] Sortie du programme.")
            break
        else:
            print("[-] Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main_menu()
