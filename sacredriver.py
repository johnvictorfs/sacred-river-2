#!/usr/bin/env python3

import random

# Local
from setinfo import read_info
from prompt import prompt
from npcs import low_level_monsters
from battle import battle
from usersave import player
import usersave
import inventory
import gameshop

__author__ = 'John Victor'
__version__ = 'Alpha 0.1'
(__description__, __long_description__) = read_info()

""" Dev Notes:

battle(player, random.choice(monster_list))  # Battle with random npc from monster_list

inv = inventory.Inventory()  # Alias of inventory.Inventory()

inv.add_item(inventory.item_var)  # Add item to inventory
inv.remove_item(inventory.item_var)  # Remove item from inventory

inv.equip_item(inventory.item_var)  # Equip item
inv.unequip_item(inventory.item_var)  # Unequip item

prompt(text, key1, key2, key3, key4 (...))  # Asks for user input with (text) and only allows user to type keys in *keys
"""

START_TEXT = f"""
 _______________________________________________________________
|                   Welcome to Sacred River 2                   |
|                                                               |
|  This is a Terminal text-based RPG game made by {__author__}.  |
|                                                               |
|_______________________________________________________________|

[ Current build: {__version__} ]
"""


def main():
    print(START_TEXT)
    prompt()


def main_menu():
    print("""
 _________________________
|        MAIN MENU        |
| [ 1 ] Shop              |
|                         |
| [ 2 ] Inventory         |
| [ 3 ] Equipment         |
| [ 4 ] Stats             |
|                         |
| [ 5 ] Explore           |
|                         |
| [ 6 ] Save              |
|                         |
| [ R ] Reset Save        |
| [ Q ] Quit              |
|_________________________|
    """)
    answer = prompt('\n>> ', '1', '2', '3', '4', '5', '6', 'r', 'R', 'q', 'Q', '')
    if answer is 'q' or answer is 'Q':
        exit(0)
    elif answer is '1':
        gameshop.display()
    elif answer is '2':
        inventory.inv.display_inventory(player)
    elif answer is '3':
        inventory.inv.display_equipment(player)
    elif answer is '4':
        player.display_stats()
    elif answer is '5':
        battle(player, random.choice(low_level_monsters))
    elif answer is '6':
        usersave.save_game()
    elif answer is 'r':
        print("Hey, i'm still working on that :/")
        print("Reset your save manually by deleting 'inventory.ini' and 'user_stats.ini' and run the game again")
        prompt()
    main_menu()


if __name__ == '__main__':
    main()
    main_menu()
