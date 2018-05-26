from clearScreen import clear_screen
from getInput import get_input
from displayStats import display_stats
from killGame import kill_game
from gameShop import display_shop
from userInventory import *

inventory = Inventory()
equipment = Equipment()


def game_menu():
    clear_screen()
    print("1: User stats")
    print("2: User inventory")
    print("3: User equipment")
    print("4: Shop")
    print("5: Exit Game (progress lost)")
    answer = get_input()
    if answer is '1':
        display_stats(player)
    elif answer is '2':
        inventory.print_items()
    elif answer is '3':
        equipment.print_equipment()
    elif answer is '4':
        bought_item = display_shop()
        inventory.add_item(bought_item)
    elif answer is '5':
        kill_game()
    else:
        print('Unexpected answer. Try again')
        return
