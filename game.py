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
        self.player = User(name='NRiver', inventory=inventory, weapon=None, armour=None)

        self.player.inventory.add(
            Armour(name='Training Armour', defence=2),
            Weapon(name='Training Sword', attack=2)
        )

        self.player.equip(inventory.items['Training Armour'])
        self.player.equip(inventory.items['Training Sword'])

        print(self.player.attack)

        self.player.unequip_weapon()

        print(self.player.attack)

        self.player.inventory.list_items()


if __name__ == "__main__":
    game = Game()
