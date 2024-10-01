import os
import webbrowser
import fade
import subprocess
import time

def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)
    print()
    
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

database_all = """
▓█████▄  ▄▄▄▄      ▓█████▄  ██▓    
▒██▀ ██▌▓█████▄    ▒██▀ ██▌▓██▒    
░██   █▌▒██▒ ▄██   ░██   █▌▒██░    
░▓█▄   ▌▒██░█▀     ░▓█▄   ▌▒██░    
░▒████▓ ░▓█  ▀█▓   ░▒████▓ ░██████▒
 ▒▒▓  ▒ ░▒▓███▀▒    ▒▒▓  ▒ ░ ▒░▓  ░
 ░ ▒  ▒ ▒░▒   ░     ░ ▒  ▒ ░ ░ ▒  ░
 ░ ░  ░  ░    ░     ░ ░  ░   ░ ░   
   ░     ░            ░        ░  ░
 ░            ░     ░              
│━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━│
│[01] -> Credit                         │
│[02] -> NazApi                         │ 
│[03] -> Fivem (2024)                   │ 
│[04] -> Minecraft                      │       
│[05] -> Discord                        │                                
│[06] -> Prevname                       │                                
│[07] -> paypal                         │                                
│[08] -> Snapchat                       │                                
│[09] -> Gmod                           │                               
│[10] -> Valorant                       │                                
│[11] -> Orange                         │                                
│[12] -> Instagram                      │                            
│[13] -> Doxbin                         │       
│[14] -> Retourner Au Multitool         │
│━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━│
"""

database_all = fade.water(database_all)

Slow(database_all)

choice = input("The number for your choice : ")

if choice == "01":
    Slow("Crédit : .gg/freeforreal (its not my database but it will come soon)")
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
elif choice == "02":
    webbrowser.open('https://mega.nz/file/trFkXIAY#sUM3Fi0L9QkshiY0uKc_nhUIkbyJ58qix3OaqcZjSlI')
    clear()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
elif choice == "03":
    webbrowser.open('https://cdn.discordapp.com/attachments/1278899112674332804/1279081742032044175/pack_fivem_2K24__2K23_by_intrable.zip?')
    clear()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
elif choice == "04":
    webbrowser.open('https://gofile.io/d/EggYGD')
    clear()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
elif choice == "05":
    webbrowser.open('https://gofile.io/d/rXKCqi')
    clear()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
elif choice == "06":
    webbrowser.open('https://cdn.discordapp.com/attachments/1273442807893458985/1276863452211580969/Prevname.rar?')
    clear()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
elif choice == "07":
    webbrowser.open('https://cdn.discordapp.com/attachments/1265006757395042324/1265007167191388170/Paypal.txt?')
    webbrowser.open('https://cdn.discordapp.com/attachments/1265006757395042324/1265007168654938173/Paypal1.txt?')
    webbrowser.open('https://cdn.discordapp.com/attachments/1265006757395042324/1265007163521368206/DB_PAYPAL_2024.txt?')
    clear()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
elif choice == "08":
    webbrowser.open('https://gofile.io/d/QzYzDt')
    clear()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
elif choice == "09":
    webbrowser.open('https://cdn.discordapp.com/attachments/1265101328401567785/1265101361054220330/gmodlife_bots.txt?')
    webbrowser.open('https://cdn.discordapp.com/attachments/1265101328401567785/1265101361523986614/payment_gmod_life.txt?')
    webbrowser.open('https://cdn.discordapp.com/attachments/1265101328401567785/1265101360592982107/email_gmod_life.txt?')
    clear()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
elif choice == "10":
    webbrowser.open('https://cdn.discordapp.com/attachments/1265008463134588948/1265008572371042346/4.6k_Valorant_Account.txt?')
    webbrowser.open('https://cdn.discordapp.com/attachments/1257370243253141525/1258323888841035796/DB_Valorant.rar?')
    clear()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
elif choice == "11":
    webbrowser.open('https://cdn.discordapp.com/attachments/1265008280586158090/1265009783547887796/orange-wanadoo1.txt?')
    webbrowser.open('https://cdn.discordapp.com/attachments/1265008280586158090/1265009783094775869/754K_HQ_FRANCE_DATABASE_ORANGE_WANADOO.txt?')
    webbrowser.open('https://cdn.discordapp.com/attachments/1265008280586158090/1265009781832159374/120k_orange.txt?')
    clear()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
elif choice == "12":
    webbrowser.open('https://gofile.io/d/cpVHO3')
    webbrowser.open('https://cdn.discordapp.com/attachments/1265008565974859887/1265012631538765945/instagram.txt?')
    clear()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
elif choice == "13":
    webbrowser.open('https://gofile.io/d/jQQkKW')
    clear()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
elif choice == "14":
    clear()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
else:
    Slow('Erreur dans le choix')
    clear()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
