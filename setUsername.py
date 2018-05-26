from clearScreen import clear_screen
from getInput import get_input


def set_username():
    clear_screen()
    print("How are you called?")
    username = get_input()
    return username
