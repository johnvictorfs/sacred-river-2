#!/usr/bin/env python

from clearScreen import clear_screen
from continueScreen import continue_screen

"""
Sequel of my terminal text-RPG game originally made in C.
But this time made in Python.

Objectives:
- To use as little non-standard resources as possible.
- Run on as many machines as possible.
- Learn stuff.
- Have fun.
"""

__author__  = "John Victor"
__version__ = "0.1"
__license__ = "MIT License"


def initial_screen():
    clear_screen()
    print(f"""
 _______________________________________________________________________
|                    Welcome to Sacred River 2!                         |
|                                                                       |
|   This is the sequel of my terminal text-RPG originally made with C.  |
|   This time in Python!                                                |
|_______________________________________________________________________|
   - Made by {__author__}.                                             
   - Version: {__version__}.                                           
""")
    continue_screen()
    return
