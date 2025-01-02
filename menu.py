from player import get_player, get_player_stats, get_player_summary, get_stats_summary
from heros import get_hero_data, get_heros, get_roles
from gamemodes_and_maps import gamemodes, maps

def menu():
    while True:
        print_main_menu()
        choice = int(input("Select an option:"))
        if choice == 0:
            print('exiting overwatch stats...')
            break #exit
        elif choice == 1:
            player_menu()
        else:
            print('invalid')



def print_main_menu():
    print("\n=== Overwatch Stats ===")
    print("--- Main Menu ---")
    print("0. Exit")
    print("1. Player Stats")
    print("2. overwatch stats")
def player_menu():
    while True:
        print_player_menu()
        choice = int(input('Select an option:'))
        if choice == 0:
            break
        elif choice == 1:
            print('finding player stats')
        elif choice == 2:
            print("finding player summary")

def print_player_menu():
    print('\n=== Overwatch Stats ===')
    print('--- Player Stats ---')
    print("0. Main Menu")
    print('1. find players stats')
    print('2. get players summary')

menu()