import os
import platform
import subprocess

def remove_discord_injections():
    injection_script_names = [
        "injection.js",
        "inject.js",
        "mod.js",
        "hack.js",
        "malicious_file.js"
    ]

    if platform.system() == "Windows":
        discord_appdata = os.path.expandvars(r"%APPDATA%\Discord")
        discord_local = os.path.expandvars(r"%LOCALAPPDATA%\Discord")
        paths_to_check = [discord_appdata, discord_local]

        for path in paths_to_check:
            if os.path.exists(path):
                for root, dirs, files in os.walk(path):
                    for file in files:
                        if file.lower() in injection_script_names:
                            try:
                                os.remove(os.path.join(root, file))
                                print(f"[+] Fichier supprimé : {file}")
                            except Exception as e:
                                print(f"[-] Erreur lors de la suppression de {file} : {str(e)}")

        subprocess.call(["taskkill", "/F", "/IM", "Discord.exe"])
        print("[+] Discord a été fermé.")

    elif platform.system() == "Linux":
        discord_dir = os.path.expanduser("~/.config/discord")
        if os.path.exists(discord_dir):
            for root, dirs, files in os.walk(discord_dir):
                for file in files:
                    if file in injection_script_names:
                        try:
                            os.remove(os.path.join(root, file))
                            print(f"[+] Fichier supprimé : {file}")
                        except Exception as e:
                            print(f"[-] Erreur lors de la suppression de {file} : {str(e)}")

        os.system("pkill Discord")
        print("[+] Discord a été fermé.")

    else:
        print("[-] Système d'exploitation non supporté.")

def display_menu():
    print("\n=== Menu de Nettoyage du Système ===")
    print("1. Supprimer les injections de Discord")
    print("2. Quitter")

def main():
    while True:
        display_menu()
        choice = input("Sélectionnez une option : ")

        if choice == '1':
            remove_discord_injections()
        elif choice == '2':
            print("[*] Processus annulé par l'utilisateur.")
            break
        else:
            print("[-] Choix non valide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
