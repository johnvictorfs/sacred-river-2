from classes import *
from getInput import get_input
from userInventory import *
from clearScreen import clear_screen

inventory = Inventory()


def display_shop():
    clear_screen()
    print("1- Iron Sword - {} gold".format(iron_sword.buy_value))
    print("2- Steel Sword - {} gold".format(steel_sword.buy_value))
    print("3- Health Potion - {} gold".format(health_potion.buy_value))
    answer = get_input()
    global buying_item
    if answer is '1':
        buying_item = iron_sword
    elif answer is '2':
        buying_item = steel_sword
    elif answer is '3':
        buying_item = health_potion
    else:
        print("Invalid answer.")
        return
    bought_item = buy(buying_item)
    return bought_item


def buy(item):
    if player.gold >= item.buy_value:
        print("Bought {}".format(item.name))
        player.gold -= item.buy_value
        print("Your gold: {}".format(player.gold))
        continue_screen()
        return item
    else:
        print("You don't have enough money for that you fool!")
        continue_screen()
        return
