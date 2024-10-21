import os
import time
import fade
import random
import string

def genSerials():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

def slow(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def spoof():
    slow(fade.water("Si vous avez des logiciels tel que voicemeeter, etc relancez le / relancez votre PC."))
    slow(fade.water("Lancement du Spoofer..."))

    os.system('Settings/Program/AMIDEWINx64.EXE /IVN "AMI"')
    os.system('Settings/Program/AMIDEWINx64.EXE /SP "System product name"')
    os.system('Settings/Program/AMIDEWINx64.EXE /SV "System product name"')
    os.system('Settings/Program/AMIDEWINx64.EXE /SS "' + genSerials() + '"')
    os.system('Settings/Program/AMIDEWINx64.EXE /SU AUTO')
    os.system('Settings/Program/AMIDEWINx64.EXE /SK "To Be Filled By O.E.M"')
    os.system('Settings/Program/AMIDEWINx64.EXE /BM "AsRock"')
    os.system('Settings/Program/AMIDEWINx64.EXE /BP "*8560M-C"')
    os.system('Settings/Program/AMIDEWINx64.EXE /BS "' + genSerials() + '"')
    os.system('Settings/Program/AMIDEWINx64.EXE /BT "Default String"')
    os.system('Settings/Program/AMIDEWINx64.EXE /BLC "Default String"')
    os.system('Settings/Program/AMIDEWINx64.EXE /CM "Default String"')
    os.system('Settings/Program/AMIDEWINx64.EXE /CV "Default String"')
    os.system('Settings/Program/AMIDEWINx64.EXE /CS "' + genSerials() + '"')
    os.system('Settings/Program/AMIDEWINx64.EXE /CA "Default String"')
    os.system('Settings/Program/AMIDEWINx64.EXE /CSK "SKU"')
    os.system('Settings/Program/AMIDEWINx64.EXE /PSN "To Be Filled By O.E.M"')
    os.system('Settings/Program/AMIDEWINx64.EXE /PAT "To Be Filled By O.E.M"')

    input(fade.water("Spoofing terminé ! Appuyez sur Entrée pour fermer le tool..."))
    os.system('python ../../main.py')

def checkSerials():
    slow(fade.water("Vérification des numéros de série du système (HWID)..."))

    os.system('title HWID CHECKER')
    os.system('color a')
    os.system('mode con: cols=90 lines=62')

    print("\033[91m-------------------------------\033[0m")
    print("\033[91m       Disk Number\033[0m")
    print("\033[91m-------------------------------\033[0m")
    os.system('wmic diskdrive get serialnumber')

    print("\033[92m-------------------------------\033[0m")
    print("\033[94m      Motherboard\033[0m")
    print("\033[92m-------------------------------\033[0m")
    os.system('wmic baseboard get serialnumber')

    print("\033[93m-------------------------------\033[0m")
    print("\033[97m        SMBios\033[0m")
    print("\033[93m-------------------------------\033[0m")
    os.system('wmic path win32_computersystemproduct get uuid')

    print("\033[94m-------------------------------\033[0m")
    print("\033[95m         GPU\033[0m")
    print("\033[94m-------------------------------\033[0m")
    os.system('wmic PATH Win32_VideoController GET Description,PNPDeviceID')

    print("\033[95m-------------------------------\033[0m")
    print("\033[93m         RAM\033[0m")
    print("\033[95m-------------------------------\033[0m")
    os.system('wmic memorychip get serialnumber')

    print("\033[96m-------------------------------\033[0m")
    print("\033[92m         Bios\033[0m")
    print("\033[96m-------------------------------\033[0m")
    os.system('wmic csproduct get uuid')

    print("\033[97m-------------------------------\033[0m")
    print("\033[95m         CPU\033[0m")
    print("\033[97m-------------------------------\033[0m")
    os.system('wmic cpu get processorid')

    print("\033[99m-------------------------------\033[0m")
    print("\033[94m         Mac Address\033[0m")
    print("\033[99m-------------------------------\033[0m")
    os.system('wmic path Win32_NetworkAdapter where "PNPDeviceID like \'%%PCI%%\' AND NetConnectionStatus=2 AND AdapterTypeID=\'0\'" get MacAddress')

    input(fade.water("Appuyez sur Entrée pour continuer..."))
    os.system('python ../../main.py')

if __name__ == "__main__":
    option = input(fade.water("Choisissez une option (1: Spoof, 2: Check HWID): "))

    if option == "1":
        spoof()
    elif option == "2":
        checkSerials()
    else:
        input(fade.fire("[x] Option invalide. Retour au menu principal."))
        os.system('python ../../main.py')
 
