# Local
from clear import clear_screen


def prompt(text="\n< Press Enter to continue. >", *keys, clear=True):
    """
    Asks user from prompt with text "text".
    Goes on if answer is present in "*keys". (use lower-cases here).
    Re-runs if a key not in "*keys" is pressed.

    Please use the format: prompt('< TEXT_HERE >', 'key1', 'key2', 'key3', clear=False/True)
    :param text: str
    :param keys: tuple of strings
    :param clear: bool
    :return: str
    """
    answer = input(text)
    if not keys:
        clear_screen()
        return answer
    if answer in keys:
        clear_screen()
        return answer
    if clear is True:
        clear_screen()
    print(f"- Error: Expected {keys} but got '{answer}' -")
    prompt()
