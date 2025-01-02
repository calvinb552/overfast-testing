import requests

def get_heros():
    hero_url = 'https://overfast-api.tekrop.fr/heroes'
    response = requests.get(hero_url)
    data = response.json()
    for i in data:
        print(i)

def get_hero_data(hero):
    hero_data_url = 'https://overfast-api.tekrop.fr/heroes/'+ hero.lower()
    response = requests.get(hero_data_url)
    hero_data = response.json()

    return hero_data

def get_roles():
    roles_url = 'https://overfast-api.tekrop.fr/roles'
    response = requests.get(roles_url)
    roles_data = response.json()
    for i in roles_data:
        print(i)
    return roles_data






