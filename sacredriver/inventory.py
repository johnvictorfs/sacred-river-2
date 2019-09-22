from dataclasses import dataclass

from sacredriver.items import Item, Equipment, Armour, Weapon
from sacredriver.utils import send


class Inventory:
    items: dict

    def __init__(self):
        self.items = {}

    def add(self, *items: Item) -> None:
        """
        Adds one or multiple of an item to a player's inventory

        If one of the same item already exists, its quantity is upped by one
        """
        for item in items:
            if self.items.get(item.name):
                self.items[item.name].quantity += 1
            else:
                self.items[item.name] = item

            send(f'Added {item.name} to inventory.')

    def remove(self, item: Item) -> None:
        if self.items.get(item.name):
            self.items[item.name].quantity -= 1

            if self.items[item.name].quantity <= 0:
                del self.items[item.name]
                send(f'Removed {item.name} from Inventory.')
                send('That was the last one.')
            else:
                send(f'Removed one of {item.name} from Inventory. ')
                send(f'You still have {self.items[item.name].quantity} remaining.')
        else:
            send(f'Couldn\'t remove {item.name} from Inventory.')

    def list_items(self) -> None:
        if not self.items:
            send('Inventory is Empty!')

        for item in self.items.values():
            send(item)
            send()
