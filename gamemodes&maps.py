import requests

def gamemodes():
    gamemode_url = 'https://overfast-api.tekrop.fr/gamemodes'
    response = requests.get(gamemode_url)
    gamemode_data = response.json()
    return gamemode_data

def maps():
    maps_url = 'https://overfast-api.tekrop.fr/maps'
    response = requests.get(maps_url)
    maps_data = response.json()
    return maps_data



