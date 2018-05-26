from clearScreen import clear_screen
from getInput import get_input
from displayStats import display_stats
from killGame import kill_game
from gameShop import display_shop
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
    if answer is '1':
        display_stats(player)
    elif answer is '2':
        inventory.print_items()
    elif answer is '3':
        display_shop()
    elif answer is '4':
        kill_game()
    else:
        print('Unexpected answer. Try again')
        return
