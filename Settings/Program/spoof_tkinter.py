import os
import random
import string
import tkinter as tk
from tkinter import messagebox

def genSerials():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

def spoof():
    os.system('spoofer/AMIDEWINx64.EXE /IVN "AMI"')
    os.system('spoofer/AMIDEWINx64.EXE /SP "System product name"')
    os.system('spoofer/AMIDEWINx64.EXE /SV "System product name"')
    os.system('spoofer/AMIDEWINx64.EXE /SS "' + genSerials() + '"')
    os.system('spoofer/AMIDEWINx64.EXE /SU AUTO')
    os.system('spoofer/AMIDEWINx64.EXE /SK "To Be Filled By O.E.M"')
    os.system('spoofer/AMIDEWINx64.EXE /BM "AsRock"')
    os.system('spoofer/AMIDEWINx64.EXE /BP "*8560M-C"')
    os.system('spoofer/AMIDEWINx64.EXE /BS "' + genSerials() + '"')
    os.system('spoofer/AMIDEWINx64.EXE /BT "Default String"')
    os.system('spoofer/AMIDEWINx64.EXE /BLC "Default String"')
    os.system('spoofer/AMIDEWINx64.EXE /CM "Default String"')
    os.system('spoofer/AMIDEWINx64.EXE /CV "Default String"')
    os.system('spoofer/AMIDEWINx64.EXE /CS "' + genSerials() + '"')
    os.system('spoofer/AMIDEWINx64.EXE /CA "Default String"')
    os.system('spoofer/AMIDEWINx64.EXE /CSK "SKU"')
    os.system('spoofer/AMIDEWINx64.EXE /PSN "To Be Filled By O.E.M"')
    os.system('spoofer/AMIDEWINx64.EXE /PAT "To Be Filled By O.E.M"')

    messagebox.showinfo("Info", "Spoofing terminé !")
    os.system('python ../../main.py')

def checkSerials():
    output = ""
    output += "-------------------------------\n"
    output += "       Disk Number\n"
    output += "-------------------------------\n"
    output += os.popen('wmic diskdrive get serialnumber').read()

    output += "\n-------------------------------\n"
    output += "      Motherboard\n"
    output += "-------------------------------\n"
    output += os.popen('wmic baseboard get serialnumber').read()

    output += "\n-------------------------------\n"
    output += "        SMBios\n"
    output += "-------------------------------\n"
    output += os.popen('wmic path win32_computersystemproduct get uuid').read()

    output += "\n-------------------------------\n"
    output += "         GPU\n"
    output += "-------------------------------\n"
    output += os.popen('wmic PATH Win32_VideoController GET Description,PNPDeviceID').read()

    output += "\n-------------------------------\n"
    output += "         RAM\n"
    output += "-------------------------------\n"
    output += os.popen('wmic memorychip get serialnumber').read()

    output += "\n-------------------------------\n"
    output += "         Bios\n"
    output += "-------------------------------\n"
    output += os.popen('wmic csproduct get uuid').read()

    output += "\n-------------------------------\n"
    output += "         CPU\n"
    output += "-------------------------------\n"
    output += os.popen('wmic cpu get processorid').read()

    output += "\n-------------------------------\n"
    output += "         Mac Address\n"
    output += "-------------------------------\n"
    output += os.popen('wmic path Win32_NetworkAdapter where "PNPDeviceID like \'%%PCI%%\' AND NetConnectionStatus=2 AND AdapterTypeID=\'0\'" get MacAddress').read()

    messagebox.showinfo("HWID Info", output)

def on_spoof():
    spoof()

def on_check_serials():
    checkSerials()

def main():
    root = tk.Tk()
    root.title("BlueTiger Spoofer")
    root.geometry("400x300")
    root.configure(bg="#e0f7fa")

    title_label = tk.Label(root, text="Choisissez une option:", font=("Helvetica", 16), bg="#e0f7fa")
    title_label.pack(pady=20)

    btn_spoof = tk.Button(root, text="Spoof", command=on_spoof, width=20, height=2, bg="#81d4fa", font=("Helvetica", 12))
    btn_spoof.pack(pady=10)

    btn_check_serials = tk.Button(root, text="Check HWID", command=on_check_serials, width=20, height=2, bg="#81d4fa", font=("Helvetica", 12))
    btn_check_serials.pack(pady=10)

    footer_label = tk.Label(root, text="© 2024 Made by Nkrz BlueTiger Spoof", font=("Helvetica", 10), bg="#e0f7fa")
    footer_label.pack(side=tk.BOTTOM, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
