from dataclasses import dataclass

from sacredriver.items import Armour, Weapon, Equipment
from sacredriver.inventory import Inventory
from sacredriver.utils import send


@dataclass
class Entity:
    name: str


@dataclass
class User(Entity):
    inventory: Inventory
    armour: Armour
    weapon: Weapon
    gold: int = 5
    health: int = 100
    base_attack: int = 1
    base_defence: int = 1

    @property
    def attack(self) -> int:
        if self.weapon:
            return self.base_attack + self.weapon.attack
        return self.base_attack

    @property
    def defence(self) -> int:
        if self.armour:
            return self.base_defence + self.armour.defence
        return self.base_defence

    def equip(self, item: Equipment) -> None:
        """
        Sets Armour or Weapon as equipped, and removes it from Inventory
        """
        if not self.inventory.items.get(item.name):
            send('You can\'t equip an item you do not have.')
            return

        if isinstance(item, Armour) or isinstance(item, Weapon):
            if isinstance(item, Armour):
                self.armour = item
            elif isinstance(item, Weapon):
                self.weapon = item
            send(f'Equipped {item.name}.')
            self.inventory.remove(item)
        else:
            send('This item cannot be equipped.')

    def unequip_weapon(self) -> None:
        """
        Unequips weapon, if Player has one equipped
        """
        if not self.weapon:
            return send('You have no Weapon equipped already.')
        send(f'Unequipped {self.weapon.name}.')
        self.inventory.add(self.weapon)
        self.weapon = None

    def unequip_armour(self):
        """
        Unequips Armour, if Player has one equipped
        """
        if not self.armour:
            return send('You have no Armour equipped already.')
        send(f'Equipped {self.armour.name}.')
        self.inventory.add(self.armour)
        self.armour = None

    def list_equipment(self):
        """
        Lists Weapon and Armour equipped
        """
        if not self.weapon and not self.armour:
            send('You have no items equipped.')

        if self.weapon:
            send(self.weapon)

        if self.armour:
            send(self.armour)


@dataclass
class Enemy(Entity):
    health: int = 10
    attack: int = 1
    defence: int = 1
    level: int = 1


@dataclass
class Goblin(Enemy):
    name: str = 'Goblin'


@dataclass
class Spider(Enemy):
    name: str = 'Spider'


@dataclass
class GiantSpider(Spider):
    name: str = 'Giant Spider'


@dataclass
class Skeleton(Enemy):
    name: str = 'Skeleton'


if __name__ == "__main__":
    user = User('nriver')
    print(user)
