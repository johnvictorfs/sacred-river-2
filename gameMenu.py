from clearScreen import clearScreen
from getInput import getInput
from displayStats import displayStats
from killGame import killGame
from classes import *


def gameMenu():
    clearScreen()
    print("1: User stats")
    print("2: User inventory")
    print("3: Shop")
    print("4: Exit Game (progress lost)")
    answer = getInput()
    if answer == '1':
        displayStats(player)
    elif answer == '2':
        print('This will display user\'s inventory')
    elif answer == '3':
        print('This will display the shop')
    elif answer == '4':
        killGame()
    else:
        print('Unexpected answer. Try again')
        return
