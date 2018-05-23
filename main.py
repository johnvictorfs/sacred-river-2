#!/usr/bin/env python

from sys import exit

"""
Sequel of my terminal text-RPG game originally made in C.
But this time made in Python.

Objectives:
- To use as little non-standard resources as possible.
- Run on as many machines as possible.
- Have fun.
"""

__author__ = 'John Victor'
__version__ = '0.1'


def killGame():
    print('--- Exiting Game ---')
    exit(0)


def continueScreen():
    try:
        input("Press enter to continue.")
    except SyntaxError:
        pass


def clearScreen():
    print('\x1b[2J')


class User(object):
    def __init__(self, name, health, attack, defence, gold):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence
        self.gold = gold


class Enemy(object):
    def __init__(self, name, health, attack, defence):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence


# Class User: Name, Health, Attack, Defence, Gold
player = User('', 100, 1, 1, 5)

# Class Enemy: Name, Health, Attack, Defence
goblin_level_2 = Enemy('Goblin (Level 2)', 30, 20, 3)
goblin_level_5 = Enemy('Goblin (Level 5)', 37, 23, 4)
spider_level_1 = Enemy('Spider (Level 3)', 20, 10, 5)
spider_level_5 = Enemy('Spider (Level 5)', 25, 15, 6)


def displayStats(character):
    clearScreen()
    print('--- Stats of {} ---'.format(character.name))
    print('Health: {}'.format(character.health))
    print('Attack: {}'.format(character.attack))
    print('Defence: {}'.format(character.defence))
    print('Gold: {}'.format(character.gold))
    print('\n')
    continueScreen()
    gameMenu()


def initialScreen():
    clearScreen()
    print("Welcome to Sacred River 2!")
    print("\n")
    print("Made by {} -  Version: {}".format(__author__, __version__))
    print("\n")
    print("The sequel of my terminal text-RPG originally made in C. This time made in Python.")
    print("\n")
    continueScreen()
    return


def getInput():
    user_input = input('\n>> ')
    return user_input


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


def setUsername():
    clearScreen()
    print("How are you called?")
    set_username = getInput()
    return set_username


initialScreen()
player.name = setUsername()
gameMenu()
