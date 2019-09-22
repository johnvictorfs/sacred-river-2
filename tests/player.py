from sacredriver.entities import User, Enemy
from sacredriver.items import Item, Armour, Weapon
from sacredriver.inventory import Inventory


def test_player():
    inventory = Inventory()
    armour = Armour(name='Training Armour', defence=2)
    weapon = Weapon(name='Training Sword', attack=2)
    player = User(name='NRiver', inventory=inventory, weapon=weapon, armour=armour, base_attack=1, base_defence=1)

    assert player.attack == 3
    assert player.defence == 3
