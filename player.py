import requests


def get_player(username):
    base_url = "https://overfast-api.tekrop.fr/players"
    parameters = {"name": username}
    response = requests.get(base_url, params=parameters)
    data = response.json()
    player_ids = []
    for p in data['results']:
        player_ids.append(p['player_id'])

    return player_ids[0]

def get_player_stats(player_id):
    player_id = get_player('litapollo')
    stats_url = 'https://overfast-api.tekrop.fr/players/litapollo-1843/summary'
    response = requests.get(stats_url)
    stats = response.json()
    return(stats)