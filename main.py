#!/usr/bin/env python

# Local imports
from classes import User, Enemy, Item, player
from userInventory import Inventory, Equipment
from gameMenu import game_menu
from setUsername import set_username
from killGame import kill_game
from __init__ import initial_screen, __author__, __version__

inventory = Inventory()

"""
Notes:
    # Clearing screen
clear_screen()

    # 'Press Enter to continue' screen
continue_screen()

    # Getting user input
get_input(message="")

    # Giving item to player
inventory.add_item(item_name)

    # Removing item from player
inventory.remove_item(item_name)
"""


def game_loop():
    while player.health > 0:
        game_menu()
    kill_game()


initial_screen()
player.name = set_username()
game_loop()
