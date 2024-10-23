import os
import platform
import subprocess

def generate_confirmation(prompt):
    confirmation = input(prompt + " (o/n) : ")
    return confirmation.lower() in ['o', 'oui']

def scan_for_malware():
    print("[*] Lancement du scan antivirus...")
    if platform.system() == "Windows":
        os.system("start /wait powershell -Command \"Start-MpScan -ScanType QuickScan\"")
        print("[+] Scan antivirus terminé.")
    elif platform.system() == "Linux":
        os.system("sudo clamscan -r / --bell -i")
        print("[+] Scan antivirus terminé.")

def check_open_ports():
    print("[*] Vérification des ports ouverts...")
    if platform.system() == "Windows":
        result = subprocess.run(["netstat", "-ano"], capture_output=True, text=True)
        print(result.stdout)
    elif platform.system() == "Linux":
        result = subprocess.run(["netstat", "-tuln"], capture_output=True, text=True)
        print(result.stdout)

def enable_firewall():
    print("[*] Activation du pare-feu...")
    if platform.system() == "Windows":
        os.system("netsh advfirewall set allprofiles state on")
        print("[+] Pare-feu Windows activé.")
    elif platform.system() == "Linux":
        os.system("sudo ufw enable")
        print("[+] Pare-feu UFW activé.")

def disable_sharing_options():
    print("[*] Désactivation des options de partage...")
    if platform.system() == "Windows":
        os.system("netsh advfirewall firewall set rule group='File and Printer Sharing' new enable=no")
        print("[+] Options de partage Windows désactivées.")
    elif platform.system() == "Linux":
        print("[+] Options de partage Linux désactivées (vérifiez vos configurations Samba).")

def secure_windows_defender():
    print("[*] Renforcement de la sécurité de Windows Defender...")
    os.system("powershell -Command \"Set-MpPreference -DisableRealtimeMonitoring $false\"")
    print("[+] Protection en temps réel activée.")

def check_windows_updates():
    print("[*] Vérification des mises à jour Windows...")
    os.system("start /wait powershell -Command \"Get-WindowsUpdate\"")
    os.system("start /wait powershell -Command \"Install-WindowsUpdate -AcceptAll -AutoReboot\"")
    print("[+] Mises à jour Windows vérifiées et installées si nécessaire.")

def check_linux_updates():
    print("[*] Vérification des mises à jour Linux...")
    os.system("sudo apt update && sudo apt upgrade -y")
    print("[+] Mises à jour Linux vérifiées et installées si nécessaire.")

def check_for_rootkits():
    print("[*] Vérification des rootkits...")
    if platform.system() == "Linux":
        os.system("sudo rkhunter --check")
        print("[+] Vérification des rootkits terminée.")

def monitor_file_integrity():
    print("[*] Surveillance de l'intégrité des fichiers...")
    if platform.system() == "Linux":
        os.system("sudo debsums -s")
        print("[+] Vérification de l'intégrité des fichiers terminée.")

def main_menu():
    while True:
        print("\n[*] Menu Principal")
        print("1. Lancer un scan antivirus")
        print("2. Vérifier les ports ouverts")
        print("3. Activer le pare-feu")
        print("4. Désactiver les options de partage")
        if platform.system() == "Windows":
            print("5. Renforcer la sécurité de Windows Defender")
            print("6. Vérifier les mises à jour Windows")
        elif platform.system() == "Linux":
            print("5. Vérifier les mises à jour Linux")
            print("6. Vérifier les rootkits")
            print("7. Surveiller l'intégrité des fichiers")
        
        print("0. Quitter")
        
        choice = input("Sélectionnez une option : ")

        if choice == '1':
            scan_for_malware()
        elif choice == '2':
            check_open_ports()
        elif choice == '3':
            enable_firewall()
        elif choice == '4':
            disable_sharing_options()
        elif choice == '5':
            if platform.system() == "Windows":
                secure_windows_defender()
            else:
                check_linux_updates()
        elif choice == '6':
            if platform.system() == "Windows":
                check_windows_updates()
            else:
                check_for_rootkits()
        elif choice == '7' and platform.system() == "Linux":
            monitor_file_integrity()
        elif choice == '0':
            print("[-] Sortie du programme.")
            break
        else:
            print("[-] Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main_menu()
