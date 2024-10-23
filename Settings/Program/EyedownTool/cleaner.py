import os
import platform
import shutil
import tempfile
import subprocess

def clean_windows():
    print("[*] Nettoyage du système Windows en cours...")
    temp_dir = tempfile.gettempdir()
    print(f"[*] Suppression des fichiers temporaires dans : {temp_dir}...")
    shutil.rmtree(temp_dir, ignore_errors=True)

    print("[*] Vidage de la corbeille...")
    subprocess.run(['PowerShell.exe', '-NoProfile', '-Command', 'Clear-RecycleBin -Confirm:$false'], check=True)

    print("[*] Suppression des fichiers inutiles dans le dossier TEMP...")
    os.system('del /q/f/s %TEMP%\\*')  

    print("[*] Suppression des fichiers temporaires dans C:\\Windows\\Temp\\...")
    os.system('del /q/f/s C:\\Windows\\Temp\\*')  

    print("[*] Nettoyage des fichiers de mise à jour dans C:\\Windows\\SoftwareDistribution\\Download\\...")
    os.system('del /q/f/s C:\\Windows\\SoftwareDistribution\\Download\\*')  

    print("[*] Nettoyage du cache Prefetch dans C:\\Windows\\Prefetch\\...")
    os.system('del /q/f/s C:\\Windows\\Prefetch\\*')  

    print("[*] Nettoyage du cache des applications dans C:\\Users\\%USERNAME%\\AppData\\Local\\...")
    os.system('del /q/f/s C:\\Users\\%USERNAME%\\AppData\\Local\\Temp\\*')  

    print("[*] Nettoyage du cache de Windows Store...")
    os.system('del /q/f/s C:\\Users\\%USERNAME%\\AppData\\Local\\Packages\\Microsoft.WindowsStore_*\\LocalCache\\*')

    print("[*] Suppression des fichiers de journaux dans C:\\Windows\\Logs\\...")
    os.system('del /q/f/s C:\\Windows\\Logs\\*')  

    print("[+] Nettoyage du système Windows terminé.")

def clean_linux():
    print("[*] Nettoyage du système Linux en cours...")
    print("[*] Suppression des fichiers temporaires dans /tmp/...") 
    os.system('rm -rf /tmp/*')  

    print("[*] Vidage de la corbeille...")
    os.system('rm -rf ~/.local/share/Trash/*')  

    print("[*] Nettoyage du cache utilisateur dans ~/.cache/...") 
    os.system('rm -rf ~/.cache/*')  

    print("[*] Suppression des fichiers de log dans /var/log/...") 
    os.system('sudo rm -rf /var/log/*')  

    print("[*] Suppression des anciens noyaux...")
    os.system('sudo apt-get autoremove --purge -y')  

    print("[*] Suppression des fichiers de sauvegarde dans ~/...")
    os.system('rm -rf ~/.*~')  

    print("[+] Nettoyage du système Linux terminé.")

def clean_system(os_name):
    if os_name == "Windows":
        clean_windows()
    elif os_name == "Linux":
        clean_linux()
    else:
        print("[-] Système d'exploitation non supporté.")

def display_menu():
    print("\n=== Menu de Nettoyage du Système ===")
    print("1. Nettoyer le système Windows")
    print("2. Nettoyer le système Linux")
    print("0. Quitter")

def main():
    while True:
        display_menu()
        choice = input("Sélectionnez une option : ")

        if choice == '1':
            clean_system("Windows")
        elif choice == '2':
            clean_system("Linux")
        elif choice == '0':
            print("[*] Processus annulé par l'utilisateur.")
            break
        else:
            print("[-] Choix non valide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
