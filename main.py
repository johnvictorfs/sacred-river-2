#!/usr/bin/env python

"""
Sequel of my terminal text-RPG game originally made in C.
But this time made in Python.

Objectives:
- To use as little non-standard resources as possible.
- Run on as many machines as possible.
- Learn stuff.
- Have fun.
"""

__author__ = 'John Victor'
__version__ = '0.1'

from classes import *
from userInventory import *
from gameMenu import game_menu
from clearScreen import clear_screen
from setUsername import set_username
from continueScreen import continue_screen
from killGame import kill_game

inventory = Inventory()

"""
Notes:
    # Clearing screen
clear_screen()

    # Press Enter to continue screen
continue_screen()

    # Giving item to player
inventory.add_item(item_name)

    # Removing item from player
inventory.remove_item(item_name)
"""


def initial_screen():
    clear_screen()
    print("Welcome to Sacred River 2!")
    print("\n")
    print("Made by {} -  Version: {}".format(__author__, __version__))
    print("\n")
    print("The sequel of my terminal text-RPG originally made in C. This time made in Python.")
    print("\n")
    continue_screen()
    return


def game_loop():
    while player.health > 0:
        game_menu()
    kill_game()


initial_screen()
player.name = set_username()
game_loop()
