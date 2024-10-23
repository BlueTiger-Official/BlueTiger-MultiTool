import os
import platform
import subprocess
import ctypes

def generate_confirmation(prompt):
    confirmation = input(prompt + " (o/n) : ")
    return confirmation.lower() in ['o', 'oui']

def clean_registry():
    print("[*] Démarrage du nettoyage complet du registre Windows.")

    if not generate_confirmation("Êtes-vous sûr de vouloir effectuer un nettoyage complet du registre Windows ?"):
        print("[-] Nettoyage du registre annulé.")
        return

    commands = [
        'reg delete HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall /f',
        'reg delete HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall /f',
        'reg delete HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\RunMRU /f',
        'reg delete HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\RunMRU /f',
        'reg delete HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* /f',
        'reg delete HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* /f',
        'reg delete HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /f',
        'reg delete HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /f',
        'reg delete HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\UserAssist /f',
        'reg delete HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\UserAssist /f'
    ]

    for command in commands:
        print(f"[*] Exécution de la commande : {command}...")
        try:
            subprocess.call(command, shell=True)
            print(f"[+] Commande exécutée avec succès : {command}")
        except Exception as e:
            print(f"[-] Erreur lors de l'exécution de {command} : {e}")

def clean_linux():
    print("[*] Démarrage du nettoyage complet pour Linux.")

    if not generate_confirmation("Êtes-vous sûr de vouloir effectuer un nettoyage complet pour Linux ?"):
        print("[-] Nettoyage Linux annulé.")
        return

    commands = [
        'rm -rf ~/.cache/*',
        'rm -rf ~/.local/share/Trash/*',
        'sudo apt-get clean',
        'sudo apt-get autoremove -y',
        'sudo journalctl --vacuum-time=7d',
        'sudo rm -rf /var/tmp/*',
        'sudo rm -rf /tmp/*',
        'sudo find /var/log -type f -name "*.log" -exec truncate -s 0 {} \;'
    ]

    for command in commands:
        print(f"[*] Exécution de la commande : {command}...")
        try:
            subprocess.call(command, shell=True)
            print(f"[+] Commande exécutée avec succès : {command}")
        except Exception as e:
            print(f"[-] Erreur lors de l'exécution de {command} : {e}")

def main():
    print("[*] Vérification du système d'exploitation...")
    if platform.system() == "Windows":
        print("[*] Système d'exploitation détecté : Windows.")
        print("[*] Vérification des droits d'administrateur...")
        if ctypes.windll.shell32.IsUserAnAdmin():
            clean_registry()
        else:
            print("[-] Ce script doit être exécuté avec des droits d'administrateur.")
    elif platform.system() == "Linux":
        print("[*] Système d'exploitation détecté : Linux.")
        clean_linux()
    else:
        print("[-] Système d'exploitation non supporté.")

if __name__ == "__main__":
    main()
