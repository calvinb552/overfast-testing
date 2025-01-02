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

def get_player_stats(username):
    player_id = get_player(username)
    stats_url = 'https://overfast-api.tekrop.fr/players/' + player_id + '/summary'
    response = requests.get(stats_url)
    stats = response.json()
    return(stats)

def get_player_summary(username):
    player_id = get_player(username)
    summary_url = 'https://overfast-api.tekrop.fr/players/'+ player_id +'/stats/summary'
    response = requests.get(summary_url)
    return(response.json())

def get_stats_summary(username, gamemode):
    player_id = get_player(username)
    parameters = {"gamemode" : gamemode}
    stat_sum_url = 'https://overfast-api.tekrop.fr/players/'+ player_id +'/stats/career'
    response = requests.get(stat_sum_url, params= parameters)
    return(response.json())