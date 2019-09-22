from clearScreen import clear_screen
from getInput import get_input


def set_username():
    clear_screen()
    username = get_input("How are you called?")
    return username
