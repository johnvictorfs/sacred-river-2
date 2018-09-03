# Local
from clear import clear_screen


def prompt(text="\n< Press Enter to continue. >", *keys, clear=True, message=True):
    """
    Asks user from prompt with text "text".
    Goes on if answer is present in "*keys". (use lower-cases here).
    Re-runs if a key not in "*keys" is pressed.

    Please use the format: prompt('< TEXT_HERE >', 'key1', 'key2', 'key3', clear=False/True, message=True/False)

    If clear is True then right after the user sends its input the screen will be cleared. It's True by default.

    'message' is the Error message when user gives an input other than the expected.
    If 'message' is False then error message will be ignored. It's True by default.

    :param text: str
    :param keys: tuple of strings
    :param clear: bool
    :param message: bool
    :return: str
    """
    answer = input(text)
    if clear is True:
        clear_screen()
    if not keys:
        return answer
    if answer in keys:
        return answer
    if message is True:
        print(f"- Error: Expected {keys} but got '{answer}' -")
    prompt()
