import os
import subprocess
import time

def Slow(texte):
    for line in texte.splitlines():
        time.sleep(0.05)

def main():
    
    seven_zip_path = r"C:\Program Files\7-Zip\7z.exe"
    if not os.path.exists(seven_zip_path):
        Slow("7-Zip n'est pas installé !")
        input("Appuyez sur une touche pour continuer...")
        return
    
    archive = input("Entrez le nom de l'archive : ")
    if not os.path.exists(archive):
        Slow("Archive introuvable !")
        input("Appuyez sur une touche pour continuer...")
        return
    
    wordlist = './Input/passlist.txt'
    if not os.path.exists(wordlist):
        Slow("Fichier de mots de passe introuvable !")
        input("Appuyez sur une touche pour continuer...")
        return
    
    Slow("Tentative de décompression en cours...")
    
    with open(wordlist, 'r') as f:
        for line in f:
            password = line.strip()
            if attempt_decompression(seven_zip_path, archive, password):
                Slow(f"Succès ! Mot de passe trouvé : {password}")
                input("Appuyez sur une touche pour continuer...")
                return
    
    Slow("Vous avez choisi une mauvaise liste de mots de passe.")
    input("Appuyez sur une touche pour continuer...")

def attempt_decompression(seven_zip_path, archive, password):
    command = [seven_zip_path, 'x', f'-p{password}', archive, '-oDecompressed by BlueTiger', '-y']
    result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0

if __name__ == "__main__":
    main()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
