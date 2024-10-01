import instaloader
import sys
import fade
import time
import os

def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)
    print()

def get_user_info(username):
    if not username:
        Slow("**Invalid Username.** \nExample: Abcdef")
        return
    
    loader = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        
        Slow(f"Profil Instagram de {fade.water(profile.username)}")
        Slow(f"Nom Complet: {fade.water(profile.full_name)}")
        Slow(f"Nom d'utilisateur: {fade.water(profile.username)}")
        Slow(f"Biographie: {fade.water(profile.biography)}")
        Slow(f"Abonnés: {fade.water(profile.followers)}")
        Slow(f"Abonnements: {fade.water(profile.followees)}")
        Slow(f"Publications: {fade.water(profile.mediacount)}")

    except Exception as e:
        Slow(f"Impossible de récupérer les informations Instagram : {fade.water(e)}")

if __name__ == "__main__":
    username = input("Entrez le nom d'utilisateur Instagram : ")
    get_user_info(username)

    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
