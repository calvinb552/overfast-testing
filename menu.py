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
        elif choice == 2:
            overwatch_menu()
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
            username = input('what is the username of the player you want to find ')
            print(get_player_stats(username))
        elif choice == 2:
            username = input('what is the username of the player you want to find ')
            print(get_player_summary(username,))
        elif choice == 3:
            username = input('what is the username of the player you want to find ')
            gamemode = input('what gamemode would you like stats for? (competitive or casual)')
            print(get_stats_summary(username, gamemode))

def print_player_menu():
    print('\n=== Overwatch Stats ===')
    print('--- Player Stats ---')
    print("0. Main Menu")
    print('1. find players stats')
    print('2. get players summary')
    print('3. get stats summary')

def overwatch_menu():
    print_overwatch_menu()
    while True:
        print_overwatch_menu()
        choice = int(input('select an option:'))
        if choice == 0:
            break
        elif choice == 1:
            print(get_heros())
        elif choice == 2:
            hero = input('what hero would you like info for?')
            print(get_hero_data(hero))
        elif choice == 3:
            print(get_roles())
        elif choice == 4:
            print(gamemodes())
        elif choice == 5:
            maps()
        else:
            print('not a valid input.')



def print_overwatch_menu():
    print('\n=== Overwatch Stats ===')
    print('--- overwatch stats ---')
    print('0. Main menu')
    print('1. Get hero list')
    print('2. Get hero details')
    print('3. get list of roles')
    print('4. get list of gamemodes')
    print('5. get list of maps')