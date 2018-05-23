from clearScreen import clearScreen
from getInput import getInput
from displayStats import displayStats
from killGame import killGame
from classes import *
from userInventory import *

inventory = Inventory()


def gameMenu():
    clearScreen()
    print("1: User stats")
    print("2: User inventory")
    print("3: Give Steel Sword")
    print("4: Exit Game (progress lost)")
    answer = getInput()
    if answer == '1':
        displayStats(player)
    elif answer == '2':
        inventory.print_items()
    elif answer == '3':
        inventory.add_item(steel_sword)
    elif answer == '4':
        killGame()
    else:
        print('Unexpected answer. Try again')
        return
