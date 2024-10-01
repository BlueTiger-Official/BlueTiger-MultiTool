import requests
import os
import fade
import time

def Slow(texte, delay=0.05):
    for char in texte:
        print(fade.water(char), end='', flush=True)
        time.sleep(delay)
    print()

def search_name(first_name, last_name):
    if not first_name or not last_name:
        Slow("Veuillez fournir à la fois un prénom et un nom de famille.")
        return
    
    try:
        api_key = "AIzaSyBfhqGOiZrUYRVI_jfprEUQ-LD9xKPJWwc"
        cx = "e711eef9dded94f7b"
        query = f"{first_name} {last_name}"
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cx}"

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            if 'items' in data:
                results = data['items']
                Slow(f"Résultats de recherche pour {first_name} {last_name}:\n")

                for result in results[:5]:
                    title = result['title']
                    snippet = result['snippet']
                    link = result['link']
                    formatted_snippet = snippet.replace('\n', ' ')
                    Slow(f"Title: {title}\nSnippet: {formatted_snippet}\nLink: {link}\n")

            else:
                Slow(f"Aucun résultat trouvé pour {first_name} {last_name}.")
        else:
            Slow(f"Erreur lors de la récupération des résultats de recherche pour {first_name} {last_name}.")
    except Exception as e:
        Slow(f"Une erreur est survenue lors de la récupération des résultats de recherche pour {first_name} {last_name}.")
        Slow(f"Détails de l'erreur: {e}")



if __name__ == "__main__":
    first_name = input(fade.water("Veuillez entrer le prénom: "))
    last_name = input(fade.water("Veuillez entrer le nom de famille: "))
    search_name(first_name, last_name)
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')