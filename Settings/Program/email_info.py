import subprocess
from emailrep import EmailRep
import re
import time
improt os
import fade

def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)
    print()

def handle_error(error_message):
    Slow(f"Error: {error_message}")

def check_email_with_holehe(email):
    try:
        output = subprocess.check_output(["C:\\Program Files\\Holehe\\holehe.exe", email]).decode("utf-8")
        output_lines = output.splitlines()
        Slow(f"\nRésultats pour l'email : {email}\n")
        for line in output_lines:
            match = re.match(r"\[\+\] Email used: .* on (.*)", line)
            if match:
                Slow(match.group(1))
    except Exception as e:
        handle_error(f"Erreur d'exécution : {str(e)}")

def get_email_information_with_emailrep(email):
    api = EmailRep()
    try:
        response = api.query(email)
        if response:
            Slow(f"\nRésultats de EmailRep :")
            Slow(f"Email: {email}")
            if 'reputation' in response:
                Slow(f"Réputation: {response['reputation']}")
            else:
                Slow(f"Réputation: N/A")
                
            if 'details' in response:
                Slow(f"Détails: {response['details']}")
                if 'sources' in response['details']:
                    Slow(f"Sources: {response['details']['sources']}")
                else:
                    Slow(f"Sources: N/A")
                Slow(f"Date de création du compte: {response['details'].get('date_creation', 'N/A')}")
                Slow(f"Dernière fois vu: {response['details'].get('last_seen', 'N/A')}")
                Slow(f"Jours depuis la dernière fois vu: {response['details'].get('days_since_last_seen', 'N/A')}")
                Slow(f"Statut de liste noire: {response['details'].get('blacklisted', 'N/A')}")
                Slow(f"Statut de malveillance: {response['details'].get('malicious_activity', 'N/A')}")
            else:
                Slow(f"Détails: N/A")
        else:
            Slow(f"Aucune information trouvée pour {email}")
    except Exception as e:
        handle_error(f"Erreur de requête : {str(e)}")

def main():
    email = input(fade.water("Entrez l'adresse email : ")).strip()
    check_email_with_holehe(email)
    get_email_information_with_emailrep(email)


if __name__ == "__main__":
    main()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
