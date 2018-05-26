from clearScreen import clear_screen
from getInput import get_input
from displayStats import display_stats
from killGame import kill_game
from classes import *
from userInventory import *

inventory = Inventory()


def game_menu():
    clear_screen()
    print("1: User stats")
    print("2: User inventory")
    print("3: Shop")
    print("4: Exit Game (progress lost)")
    answer = get_input()
    if answer == '1':
        display_stats(player)
    elif answer == '2':
        inventory.print_items()
    elif answer == '3':
        print('this will be a shop.')
        inventory.add_item(iron_sword)
        inventory.add_item(health_potion)
    elif answer == '4':
        kill_game()
    else:
        print('Unexpected answer. Try again')
        return
