import requests
import fade
import time
import os

API_KEY = "38DFAEE6ACA6F68021865A766C7671DF"

def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)
    print()

def get_steam_user_info_by_id(steam_id):
    url = "https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/"
    params = {
        "key": API_KEY,
        "steamids": steam_id
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        user_info = response.json().get('response', {}).get('players', [])
        
        if not user_info:
            return {"Error": "No user found with this Steam ID."}

        return user_info[0]
    except requests.exceptions.RequestException as e:
        return {"Error": str(e)}

def get_owned_games(steam_id):
    url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"
    params = {
        "key": API_KEY,
        "steamid": steam_id,
        "include_appinfo": True,
        "include_played_free_games": True
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        games_info = response.json().get('response', {}).get('games', [])
        
        if not games_info:
            return {"Error": "No games found for this Steam ID."}

        return games_info
    except requests.exceptions.RequestException as e:
        return {"Error": str(e)}

def main():
    choice = input("Enter 1 to search by Steam ID: ").strip()

    if choice == '1':
        steam_id = input("Enter the Steam ID: ").strip()
        user_data = get_steam_user_info_by_id(steam_id)
        
        if "Error" in user_data:
            Slow(f"Error: {user_data['Error']}")
            return

        Slow("\nSteam User Information:")
        for key, value in user_data.items():
            Slow(f"{key}: {value}")

        games_data = get_owned_games(steam_id)
        
        if "Error" in games_data:
            Slow(f"\nError: {games_data['Error']}")
        else:
            Slow("\nGames Owned:")
            for game in games_data:
                Slow(f"- {game['name']} (Playtime: {game['playtime_forever']} minutes)")

    else:
        Slow("Invalid choice. Please enter 1.")
        return

if __name__ == "__main__":
    main()
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')
