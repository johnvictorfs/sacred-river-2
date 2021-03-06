from player import Player
import configparser
import inventory
from prompt import prompt

STATUS_FILE = 'user_stats.ini'
INVENTORY_FILE = 'inventory.ini'


def settings_exist(file=STATUS_FILE):
    """
    Verifies if 'settings.ini' file exists or not.
    :return: bool
    """
    try:
        with open(file, 'r'):
            return True
    except FileNotFoundError:
        return False


def read_save_status(file=STATUS_FILE):
    status_file = configparser.ConfigParser()
    status_file.read(file)

    user_name = status_file['USER_STATS']['name']
    user_attack = status_file['USER_STATS']['attack']
    user_defence = status_file['USER_STATS']['defence']
    user_health = status_file['USER_STATS']['health']
    user_gold = status_file['USER_STATS']['gold']
    user_luck = status_file['USER_STATS']['luck']

    player_save = Player(user_name, user_attack, user_defence, user_health, user_gold, user_luck)

    return player_save


def read_inventory_status(file=INVENTORY_FILE):
    inventory_file = configparser.ConfigParser()
    inventory_file.read(file)

    try:
        for key in inventory_file['USER_INVENTORY']:
            for item in inventory.item_list:
                if str(key) == str(item.id):
                    for quantity in range(int(inventory_file['USER_INVENTORY'][key])):
                        inventory.inv.add_item(item, message=False)
        for key in inventory_file['USER_EQUIPMENT']:
            for item in inventory.item_list:
                if str(key) == str(item.id):
                    inventory.inv.add_item(item, message=False)
                    inventory.inv.equip_item(item, message=False)
    except KeyError:
        return


def create_save(name):
    config = configparser.ConfigParser()
    config['USER_STATS'] = {
        'name': name,
        'attack': 10,
        'defence': 0,
        'health': 50,
        'gold': 20,
        'luck': 1
    }

    if settings_exist(file=STATUS_FILE):
        player_save = read_save_status()
        return player_save
    else:
        with open(STATUS_FILE, 'w') as config_file:
            config.write(config_file)
            return


def create_user_data():
    if settings_exist():
        user = read_save_status(file=STATUS_FILE)
        read_inventory_status()
        if user.health <= 0:
            create_save(user.name)
            user = read_save_status(file=STATUS_FILE)
            return user
        return user
    else:
        user_name = prompt("\n< How are you called? >\n\n>> ")
        create_save(user_name)
        user = read_save_status(file=STATUS_FILE)
    return user


def save_stats():
    config = configparser.ConfigParser()

    config['USER_STATS'] = {
        'name': player.name,
        'attack': player.attack,
        'defence': player.defence,
        'health': player.health,
        'gold': player.gold,
        'luck': player.luck
    }
    with open(STATUS_FILE, 'w') as config_file:
        config.write(config_file)


def save_inventory():
    config = configparser.ConfigParser()

    config['USER_INVENTORY'] = {}
    config['USER_EQUIPMENT'] = {}

    for item in inventory.inv.items.values():
        config['USER_INVENTORY'][str(item.id)] = str(item.quantity)

    for item in inventory.inv.equipment.values():
        config['USER_EQUIPMENT'][str(item.id)] = str(item.item_type)

    with open('inventory.ini', 'w') as config_file:
        config.write(config_file)


def save_game():
    print("[[[ Saving game... ]]]")
    save_stats()
    save_inventory()
    print("[ Game Saved ]")
    prompt()


player = create_user_data()
