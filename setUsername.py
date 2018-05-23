from clearScreen import clearScreen
from getInput import getInput


def setUsername():
    clearScreen()
    print("How are you called?")
    set_username = getInput()
    return set_username
