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
from gameMenu import gameMenu
from clearScreen import clearScreen
from setUsername import setUsername
from continueScreen import continueScreen
from killGame import killGame
from userInventory import *

inventory = Inventory()


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


def gameLoop():
    while player.health > 0:
        gameMenu()
    killGame()


initialScreen()
player.name = setUsername()
gameLoop()
