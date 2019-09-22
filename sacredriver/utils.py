def send(message: str or object = None) -> None:
    """
    Wraps all game messages to a print, used so if the game ever
    becomes a GUI game, it's easier to change Game Messages to another
    format
    """
    if not message:
        return print()
    return print(message)
