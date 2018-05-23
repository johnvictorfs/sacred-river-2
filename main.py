#!/usr/bin/env python

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


def clearScreen():
    print('\x1b[2J')


def continueScreen():
    try:
        input("Press enter to continue.")
    except SyntaxError:
        pass


def initialScreen():
    clearScreen()
    print("Welcome to Sacred River 2!")
    print("\n")
    print("Made by {} -  Version: {}".format(__author__, __version__))
    print("\n")
    print("The sequel of my terminal text-RPG originally made in C. This time made in Python.")
    print("\n")
    continueScreen()


def gameMenu():
    clearScreen()
    print("This will be a Menu")


initialScreen()
gameMenu()
