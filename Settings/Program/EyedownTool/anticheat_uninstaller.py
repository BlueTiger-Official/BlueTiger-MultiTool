import os
import subprocess
import platform

def uninstall_anti_cheat_windows(cheat_name):
    print(f"[*] Tentative de désinstallation de {cheat_name}...")
    try:
        subprocess.call(['wmic', 'product', 'where', f'name="{cheat_name}"', 'call', 'uninstall'])
        print(f"[+] {cheat_name} désinstallé avec succès.")
    except Exception as e:
        print(f"[-] Échec de la désinstallation de {cheat_name}: {str(e)}")

def uninstall_anti_cheat_linux(cheat_name):
    print(f"[*] Tentative de désinstallation de {cheat_name}...")
    try:
        subprocess.call(['sudo', 'apt-get', 'remove', '--purge', cheat_name])
        print(f"[+] {cheat_name} désinstallé avec succès.")
    except Exception as e:
        print(f"[-] Échec de la désinstallation de {cheat_name}: {str(e)}")

def display_menu():
    anti_cheat_list = [
        "BattleEye",
        "EasyAntiCheat",
        "Ricochet",
        "Vanguard",
        "PunkBuster",
        "XIGNCODE",
        "FairFight",
        "HVM"
    ]

    print("\n=== Menu de Désinstallation d'Anti-Cheat ===")
    for index, cheat in enumerate(anti_cheat_list):
        print(f"{index + 1}. {cheat}")
    print("0. Quitter")

    return anti_cheat_list

def main():
    while True:
        anti_cheat_list = display_menu()
        try:
            choice = int(input("Entrez le numéro de l'anti-cheat à désinstaller (0 pour quitter) : ")) - 1

            if choice == -1:
                print("[*] Processus annulé par l'utilisateur.")
                break

            if choice < 0 or choice >= len(anti_cheat_list):
                print("[-] Choix non valide. Veuillez réessayer.")
                continue

            cheat_name = anti_cheat_list[choice]

            if platform.system() == "Windows":
                print("[*] Démarrage du processus de désinstallation des anti-triches sur Windows...")
                uninstall_anti_cheat_windows(cheat_name)
            elif platform.system() == "Linux":
                print("[*] Démarrage du processus de désinstallation des anti-triches sur Linux...")
                uninstall_anti_cheat_linux(cheat_name)
            else:
                print("[-] Système d'exploitation non supporté.")

        except ValueError:
            print("[-] Veuillez entrer un numéro valide.")

    print("[*] Processus de désinstallation terminé.")

if __name__ == "__main__":
    main()
