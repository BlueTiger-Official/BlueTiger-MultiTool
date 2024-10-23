import subprocess
import platform

def uninstall_windows_defender():
    print("[*] Tentative de désinstallation de Windows Defender...")
    try:
        subprocess.call(['powershell', '-Command', 'Uninstall-WindowsFeature', '-Name', 'Windows-Defender-Features'])
        print("[+] Windows Defender désinstallé avec succès.")
    except Exception as e:
        print(f"[-] Échec de la désinstallation de Windows Defender: {str(e)}")

def main_menu():
    while True:
        print("\n[*] Menu Principal")
        print("1. Désinstaller Windows Defender")
        print("0. Quitter")

        choice = input("Sélectionnez une option : ")

        if choice == '1':
            if platform.system() == "Windows":
                uninstall_windows_defender()
            else:
                print("[-] Ce script ne peut être exécuté que sur Windows.")
        elif choice == '0':
            print("[-] Sortie du programme.")
            break
        else:
            print("[-] Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main_menu()
