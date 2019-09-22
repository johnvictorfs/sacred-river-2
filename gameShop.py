import classes
from continueScreen import continue_screen
from getInput import get_input
from userInventory import Inventory, Equipment
from clearScreen import clear_screen

inventory = Inventory()


def display_shop():
    clear_screen()
    print(f"1- Iron Sword - {classes.iron_sword.buy_value} gold")
    print(f"2- Steel Sword - {classes.steel_sword.buy_value} gold")
    print(f"3- Health Potion - {classes.health_potion.buy_value} gold")
    answer = get_input()
    global buying_item
    if answer is '1':
        buying_item = classes.iron_sword
    elif answer is '2':
        buying_item = classes.steel_sword
    elif answer is '3':
        buying_item = classes.health_potion
    else:
        print("Invalid answer.")
        return
    bought_item = buy(buying_item)
    return bought_item


def buy(item):
    if classes.player.gold >= item.buy_value:
        print("Bought {}".format(item.name))
        classes.player.gold -= item.buy_value
        print("Your gold: {}".format(classes.player.gold))
        continue_screen()
        return item
    else:
        print("You don't have enough money for that you fool!")
        continue_screen()
        return
