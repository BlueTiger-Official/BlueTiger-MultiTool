import requests
import re
import fade
import time
import os

def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)
    print()

def scrape_cfx_ids(url, output_file):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            cfx_ids = re.findall(r'\u0006([a-z0-9]{6})', response.text)

            if cfx_ids:
                with open(output_file, 'w') as file:
                    for cfx_id in cfx_ids:
                        file.write(cfx_id + '\n')
                Slow(f"{len(cfx_ids)} IDs trouvés et enregistrés dans {output_file}.")
            else:
                Slow("Aucun ID trouvé.")
        else:
            Slow(f"Erreur lors de la requête: {response.status_code}")

    except Exception as e:
        Slow(f"Une erreur est survenue: {e}")

url = "https://servers-frontend.fivem.net/api/servers/streamRedir/"
output_file = os.path.join('..', '..', 'Input', 'Serveur.txt')
scrape_cfx_ids(url, output_file)

input("[x] Appuyer sur entrée pour retourner au menu principal.")
os.system('python ../../main.py')
