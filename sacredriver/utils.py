def send(message: str or object) -> None:
    """
    Wraps all game messages to a print, used so if the game ever
    becomes a GUI game, it's easier to change Game Messages to another
    format
    """
    print(message)
