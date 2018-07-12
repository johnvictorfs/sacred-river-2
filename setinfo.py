import configparser

INFO_FILE = 'info.ini'


def read_info():
    """
    Reads info from 'info.ini' and returns them all into a tuple.
    :return: tuple
    """
    info = configparser.ConfigParser()
    info.read(INFO_FILE)
    description = info['COMMON']['description']
    long_description = info['COMMON']['long_description']
    return description, long_description
