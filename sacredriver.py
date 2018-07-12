#!/usr/bin/env python3

import random

# Local
from setinfo import read_info
from prompt import prompt
from npcs import monster_list
from battle import battle
from userstats import player
import userstats
import inventory
import gameshop

__author__ = 'John Victor'
__version__ = '0.1'
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
- Welcome to Sacred River 2 - 
This is a Terminal text-based RPG game made by {__author__}.

Current build: {__version__}
"""
inv = inventory.Inventory()


def main():
    print(START_TEXT)
    prompt()


def main_menu():
    print('--- Main menu ---')
    print('-1: Game Shop')
    print('-2: Inventory')
    print('-3: Equipment')
    print('-4: Stats')
    print('-5: Fight Monsters')
    print('-6: Save Game (WARNING - ONLY STATS ARE SAVED FOR NOW)')
    print("-Q: Exit Game")
    answer = prompt('\n>> ', '1', '2', '3', '4', '5', '6', 'q', 'Q', '', clear=False)
    if answer is '1':
        bought_item = gameshop.display()
        try:
            inv.add_item(bought_item)
        except AttributeError:
            pass
    elif answer is '2':
        inv.display_inventory(player)
    elif answer is '3':
        inv.display_equipment(player)
    elif answer is '4':
        player.display()
    elif answer is '5':
        battle(player, random.choice(monster_list))
    elif answer is '6':
        userstats.save_game()
    elif answer is 'q':
        exit(0)
    main_menu()


if __name__ == '__main__':
    main()
    inv.add_item(inventory.iron_sword)
    main_menu()
