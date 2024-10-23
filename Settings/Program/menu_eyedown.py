import subprocess
import os
import fade
import colorama

colorama.init(autoreset=True)
color = colorama.Fore
blue = color.BLUE

def format_option(script_name):
    return os.path.basename(script_name).replace('.py', '').replace('_', ' ').title()

def display_menu():
    scripts = {
        '01': 'Settings/Program/EyedownTool/anticheat_uninstaller.py',
        '02': 'Settings/Program/EyedownTool/app_uninstaller_optimizer.py',
        '03': 'Settings/Program/EyedownTool/cleaner.py',
        '04': 'Settings/Program/EyedownTool/data_collection.py',
        '05': 'Settings/Program/EyedownTool/discord_inject_remover.py',
        '06': 'Settings/Program/EyedownTool/disk_cleaner.py',
        '07': 'Settings/Program/EyedownTool/file_decryption.py',
        '08': 'Settings/Program/EyedownTool/file_encryption.py',
        '09': 'Settings/Program/EyedownTool/full_confidentiality.py',
        '10': 'Settings/Program/EyedownTool/registery_cleaner.py',
        '11': 'Settings/Program/EyedownTool/system_security.py',
        '12': 'Settings/Program/EyedownTool/telemetry_remover.py',
        '13': 'Settings/Program/EyedownTool/website_unlocker.py',
        '14': 'Settings/Program/EyedownTool/win_defender_uninstall.py',
    }

    print(f"{blue}Eye Down Tool - Menu")
    print(f"{blue}---------------------")
    
    for key, script in scripts.items():
        print(f"{blue}{key}: {format_option(script)}")

def execute_script(option):
    scripts = {
        '01': 'Settings/Program/EyedownTool/anticheat_uninstaller.py',
        '02': 'Settings/Program/EyedownTool/app_uninstaller_optimizer.py',
        '03': 'Settings/Program/EyedownTool/cleaner.py',
        '04': 'Settings/Program/EyedownTool/data_collection.py',
        '05': 'Settings/Program/EyedownTool/discord_inject_remover.py',
        '06': 'Settings/Program/EyedownTool/disk_cleaner.py',
        '07': 'Settings/Program/EyedownTool/file_decryption.py',
        '08': 'Settings/Program/EyedownTool/file_encryption.py',
        '09': 'Settings/Program/EyedownTool/full_confidentiality.py',
        '10': 'Settings/Program/EyedownTool/registery_cleaner.py',
        '11': 'Settings/Program/EyedownTool/system_security.py',
        '12': 'Settings/Program/EyedownTool/telemetry_remover.py',
        '13': 'Settings/Program/EyedownTool/website_unlocker.py',
        '14': 'Settings/Program/EyedownTool/win_defender_uninstall.py',
    }

    if option in scripts:
        script_path = scripts[option]
        try:
            subprocess.run(['python', script_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Une erreur s'est produite lors de l'exécution de {script_path} : {e}")
    else:
        print("Aucun script associé à cette option.")

def main():
    while True:
        display_menu()
        choice = input("Veuillez entrer votre choix : ").strip().upper()

        if choice.isdigit() and (1 <= int(choice) <= 14 or choice in [str(i).zfill(2) for i in range(1, 15)]):
            option = choice.zfill(2)
            execute_script(option)  
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
