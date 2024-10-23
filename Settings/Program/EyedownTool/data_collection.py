import os
import platform
import shutil

def clear_temp_files(os_name):
    print("[*] Suppression des fichiers temporaires...")
    if os_name == "Windows":
        temp_dirs = [
            os.path.join(os.getenv('TEMP')),
            os.path.join(os.getenv('USERPROFILE'), 'AppData', 'Local', 'Temp'),
            'C:\\Windows\\Temp'
        ]
    elif os_name == "Linux":
        temp_dirs = [
            '/tmp',
            '/var/tmp',
            os.path.join(os.getenv('HOME'), '.cache')
        ]
    else:
        print("[-] Système d'exploitation non supporté.")
        return

    for temp_dir in temp_dirs:
        print(f"[*] Suppression de : {temp_dir}...")
        try:
            shutil.rmtree(temp_dir, ignore_errors=True)
        except Exception as e:
            print(f"[-] Erreur lors de la suppression de {temp_dir}: {e}")

def remove_microsoft_data():
    print("[*] Suppression des données de collecte Microsoft...")
    microsoft_data_paths = [
        "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\*",
        "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\*",
        "C:\\ProgramData\\Microsoft\\Windows\\WER\\ReportArchive\\*",
        "C:\\ProgramData\\Microsoft\\Windows\\Telemetry\\*",
        "C:\\ProgramData\\Microsoft\\Windows\\Caches\\*",
        "C:\\Users\\Public\\Documents\\Microsoft Shared\\Windows\\*",
        "C:\\ProgramData\\Microsoft\\Windows\\WER\\ReportQueue\\*",
        "C:\\ProgramData\\Microsoft\\Windows\\SystemData\\*"
    ]

    for path in microsoft_data_paths:
        print(f"[*] Suppression de : {path}...")
        try:
            shutil.rmtree(path, ignore_errors=True)
        except Exception as e:
            print(f"[-] Erreur lors de la suppression de {path}: {e}")

def remove_nvidia_data():
    print("[*] Suppression des données de collecte Nvidia...")
    nvidia_data_paths = [
        "C:\\ProgramData\\NVIDIA Corporation\\NV_Cache\\*",
        "C:\\ProgramData\\NVIDIA Corporation\\NetService\\*",
        "C:\\ProgramData\\NVIDIA Corporation\\NvTelemetry\\*",
        "C:\\ProgramData\\NVIDIA Corporation\\GPU Temp\\*",
        "C:\\ProgramData\\NVIDIA Corporation\\Installer2\\*",
        "C:\\ProgramData\\NVIDIA Corporation\\NVIDIA Update Core\\*"
    ]

    for path in nvidia_data_paths:
        print(f"[*] Suppression de : {path}...")
        try:
            shutil.rmtree(path, ignore_errors=True)
        except Exception as e:
            print(f"[-] Erreur lors de la suppression de {path}: {e}")

def clear_logs(os_name):
    print("[*] Suppression des fichiers de logs...")
    if os_name == "Windows":
        log_paths = [
            "C:\\Windows\\Logs\\*",
            "C:\\ProgramData\\Microsoft\\Windows\\WER\\ReportArchive\\*",
            "C:\\Windows\\Minidump\\*",
            "C:\\Windows\\Memory.dmp"
        ]
    elif os_name == "Linux":
        log_paths = [
            '/var/log/*',
            os.path.join(os.getenv('HOME'), '.*log')
        ]
    else:
        print("[-] Système d'exploitation non supporté.")
        return

    for path in log_paths:
        print(f"[*] Suppression de : {path}...")
        try:
            shutil.rmtree(path, ignore_errors=True)
        except Exception as e:
            print(f"[-] Erreur lors de la suppression de {path}: {e}")

def clean_system(os_name):
    clear_temp_files(os_name)
    remove_microsoft_data()
    remove_nvidia_data()
    clear_logs(os_name)
    print("[+] Nettoyage du système terminé.")

def display_menu():
    print("\n=== Menu de Nettoyage du Système ===")
    print("1. Supprimer les fichiers temporaires")
    print("2. Supprimer les données Microsoft")
    print("3. Supprimer les données Nvidia")
    print("4. Supprimer les fichiers de logs")
    print("5. Nettoyer tout le système")
    print("0. Quitter")

def main():
    os_name = platform.system()
    
    while True:
        display_menu()
        choice = input("Sélectionnez une option : ")

        if choice == '1':
            clear_temp_files(os_name)
        elif choice == '2':
            remove_microsoft_data()
        elif choice == '3':
            remove_nvidia_data()
        elif choice == '4':
            clear_logs(os_name)
        elif choice == '5':
            clean_system(os_name)
        elif choice == '0':
            print("[*] Processus annulé par l'utilisateur.")
            break
        else:
            print("[-] Choix non valide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
