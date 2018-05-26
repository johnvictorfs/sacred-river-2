from continueScreen import continue_screen
from getInput import get_input
from classes import *


class Inventory(object):
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item
        print('Added {} to inventory.'.format(item.name))

    def remove_item(self, item):
        del self.items[item.name]
        print('Removed {} from inventory.'.format(item.name))

    def print_items(self):
        if not self.items.values():
            print('\nInventory is Empty!\n')
        for item in self.items.values():
            print('Name: {}'.format(item.name))
            if item.attack > 0:
                print('Attack: +{}'.format(item.attack))
            if item.armour > 0:
                print('Armour: +{}'.format(item.armour))
            if item.heal > 0:
                print('Heal: {} HP'.format(item.heal))
            print('Buy Value: {} coins'.format(item.buy_value))
            print('Sell Value: {} coins'.format(item.sell_value))

            print('\n')
        continue_screen()
        return


inventory = Inventory()


class Equipment(object):
    def __init__(self):
        self.equipped_items = {}

    def equip_item(self, item):
        if item.attack > 0 or item.armour > 0:
            inventory.remove_item(item)
            self.equipped_items[item.name] = item
            print("Equipped {}.")
            player.attack += item.attack
            player.defence += item.armour
        else:
            print("Item is not a Weapon nor a piece of Armour you fool.")
            return

    def unequip_item(self, item):
        del self.equipped_items[item.name]
        print('Unequipped {}.'.format(item.name))
        player.attack -= item.attack
        player.defence -= item.armour

    def print_equipment(self):
        if not self.equipped_items.values():
            print('\nYou have no items equipped!\n')
        for item in self.equipped_items.values():
            print('Name: {}'.format(item.name))
            if item.attack > 0:
                print('Attack: +{}'.format(item.attack))
            if item.armour > 0:
                print('Armour: +{}'.format(item.armour))
            print('Buy Value: {} coins'.format(item.buy_value))
            print('Sell Value: {} coins'.format(item.sell_value))
        print('\n')
        continue_screen()
