from typing import List

from sacredriver.entities import User, Enemy
from sacredriver.items import Item, Armour, Weapon
from sacredriver.inventory import Inventory


class Game:
    player: User
    enemies: List[Enemy]
    items: List[Item]

    def __init__(self):
        inventory = Inventory()
        armour = Armour(name='Training Armour', defence=2)
        weapon = Weapon(name='Training Sword', attack=2)
        self.player = User(name='NRiver', inventory=inventory, weapon=weapon, armour=armour)
        print(self.player.attack)


if __name__ == "__main__":
    game = Game()
