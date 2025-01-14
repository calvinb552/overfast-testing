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
    abilities = hero_data['abilities'] #list
    if len(abilities) == 3:
        ability_one = abilities[0]
        ability_two = abilities[1]
        ability_three = abilities[2]

        ability_one_info = "\nName: " + ability_one['name'] + "\nDescription: " + ability_one['description']
        ability_two_info = "\nName: " + ability_two['name'] + "\nDescription: " + ability_two['description']
        ability_three_info = "\nName: " + ability_three['name'] + "\nDescription: " + ability_three['description']
        ability_info = "Ability one: " + ability_one_info + "\nAbility two: " + ability_two_info + "\nAbility three: " + ability_three_info

    elif len(abilities) == 4:
        ability_one = abilities[0]
        ability_two = abilities[1]
        ability_three = abilities[2]
        ability_four = abilities[3]

        ability_one_info = "\nName: " + ability_one['name'] + "\nDescription: " + ability_one['description']
        ability_two_info = "\nName: " + ability_two['name'] + "\nDescription: " + ability_two['description']
        ability_three_info = "\nName: " + ability_three['name'] + "\nDescription: " + ability_three['description']
        ability_four_info = "\nName: " + ability_four['name'] + "\nDescription: " + ability_four['description']
        ability_info = "Ability one: " + ability_one_info + "\nAbility two: " + ability_two_info + "\nAbility three: " + ability_three_info + "\nAbility four: " + ability_four_info
    elif len(abilities) == 5:
        ability_one = abilities[0]
        ability_two = abilities[1]
        ability_three = abilities[2]
        ability_four = abilities[3]
        ability_five = abilities[4]

        ability_one_info = "\nName: " + ability_one['name'] + "\nDescription: " + ability_one['description']
        ability_two_info = "\nName: " + ability_two['name'] + "\nDescription: " + ability_two['description']
        ability_three_info = "\nName: " + ability_three['name'] + "\nDescription: " + ability_three['description']
        ability_four_info = "\nName: " + ability_four['name'] + "\nDescription: " + ability_four['description']
        ability_five_info = "\nName: " + ability_five['name'] + "\nDescription: " + ability_five['description']
        ability_info = "Ability one: " + ability_one_info + "\nAbility two: " + ability_two_info + "\nAbility three: " + ability_three_info + "\nAbility four: " + ability_four_info +"\nAbility five: " + ability_five_info
    elif len(abilities) == 6:
        ability_one = abilities[0]
        ability_two = abilities[1]
        ability_three = abilities[2]
        ability_four = abilities[3]
        ability_five = abilities[4]
        ability_six = abilities[5]

        ability_one_info = "\nName: " + ability_one['name'] + "\nDescription: " + ability_one['description']
        ability_two_info = "\nName: " + ability_two['name'] + "\nDescription: " + ability_two['description']
        ability_three_info = "\nName: " + ability_three['name'] + "\nDescription: " + ability_three['description']
        ability_four_info = "\nName: " + ability_four['name'] + "\nDescription: " + ability_four['description']
        ability_five_info = "\nName: " + ability_five['name'] + "\nDescription: " + ability_five['description']
        ability_six_info = "\nName: " + ability_six['name'] + "\nDescription: " + ability_six['description']
        ability_info = "Ability one: " + ability_one_info + "\nAbility two: " + ability_two_info + "\nAbility three: " + ability_three_info + "\nAbility four: " + ability_four_info +"\nAbility five: " + ability_five_info + "\nAbility six: " + ability_six_info
    return "Name: " + hero_data['name'] + "\nDiscription: " + hero_data['description'] + "\nRole: " + hero_data['role'] + "\nLocation: " + hero_data['location'] + "\nAge: " + str(hero_data['age']) + "\nBirthday: " + hero_data['birthday'] + "\nHitpoints: " + str(hero_data['hitpoints']) + "abilities:\n" + ability_info
            

def get_roles():
    roles_url = 'https://overfast-api.tekrop.fr/roles'
    response = requests.get(roles_url)
    roles_data = response.json()
    for i in roles_data:
        print(i)
    return roles_data









