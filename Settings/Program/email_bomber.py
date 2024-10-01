import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re
import fade
import time

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)
    print()

def send_email(sender_email, password, receiver_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        return 'Email envoyé avec succès !'
    except Exception as e:
        return f'Erreur : {e}'

def main():
    email_data = {}

    art_ascii = """
▓█████  ███▄ ▄███▓ ▄▄▄       ██▓ ██▓        ▄▄▄▄    ▒█████   ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███  
▓█   ▀ ▓██▒▀█▀ ██▒▒████▄    ▓██▒▓██▒       ▓█████▄ ▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒
▒███   ▓██    ▓██░▒██  ▀█▄  ▒██▒▒██░       ▒██▒ ▄██▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒
▒▓█  ▄ ▒██    ▒██ ░██▄▄▄▄██ ░██░▒██░       ▒██░█▀  ▒██   ██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  
░▒████▒▒██▒   ░██▒ ▓█   ▓██▒░██░░██████▒   ░▓█  ▀█▓░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒
░░ ▒░ ░░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░▓  ░   ░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ░ ░  ░░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░ ▒  ░   ▒░▒   ░   ░ ▒ ▒░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░
   ░   ░      ░     ░   ▒    ▒ ░  ░ ░       ░    ░ ░ ░ ░ ▒  ░      ░    ░    ░    ░     ░░   ░ 
   ░  ░       ░         ░  ░ ░      ░  ░    ░          ░ ░         ░    ░         ░  ░   ░     
                                                 ░                           ░                 
                        Made by Nkrz.dll
    """
    art_ascii_fade = fade.water(art_ascii)
    Slow(art_ascii_fade)
    Slow("Veuillez fournir l'adresse email du destinataire : ")
    email_data['receiver'] = input(fade.water("> "))
    
    Slow("Veuillez fournir l'adresse email de l'expéditeur (la tienne) : ")
    email_data['sender'] = input(fade.water("> "))
    
    Slow("Veuillez fournir le mot de passe de l'adresse email de l'expéditeur (la tienne) : ")
    email_data['password'] = input(fade.water("> "))
    
    Slow("Veuillez fournir le sujet de l'email : ")
    email_data['subject'] = input(fade.water("> "))
    
    Slow("Veuillez fournir le corps de l'email : ")
    email_data['body'] = input(fade.water("> "))

    try:
        num_times = int(input(fade.water("Combien de fois souhaitez-vous envoyer cet email ? ")))
    except ValueError:
        Slow("Veuillez entrer un nombre valide.")
        return
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email_data['receiver']) or not re.match(r"[^@]+@[^@]+\.[^@]+", email_data['sender']):
        Slow("Format d'adresse email invalide.")
        return

    for _ in range(num_times):
        response = send_email(
            email_data['sender'],
            email_data['password'],
            email_data['receiver'],
            email_data['subject'],
            email_data['body']
        )
        Slow(response)

if __name__ == "__main__":
    main()
import os    
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
