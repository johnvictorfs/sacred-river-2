import configparser

# Local
from prompt import prompt
from clear import clear_screen


class Item:

    def __init__(self, name, id, attack=0, armour=0, buy_value=0, sell_value=0, heal_value=0, item_type='', quantity=0):
        """
        Item type can be: "Weapon", "Armour", "Health_Potion"

        :param name: str
        :param id: int
        :param attack: int
        :param armour: int
        :param buy_value: int
        :param sell_value: int
        :param heal_value: int
        :param item_type: str
        """
        self.name = name
        self.id = id
        self.attack = attack
        self.armour = armour
        self.buy_value = buy_value
        self.sell_value = sell_value
        self.heal_value = heal_value
        self.item_type = item_type
        self.quantity = quantity


class Inventory:

    def __init__(self):
        self.items = {}
        self.equipment = {}
        self.weapon_equipped = False
        self.armour_equipped = False

    def add_item(self, item, message=True):
        self.items[item.name] = item
        item.quantity += 1

        if message is True:
            print(f"Added {item.name} to Inventory.")

    def remove_item(self, item, message=True):
        if item.name in self.items:
            item.quantity -= 1
            if item.quantity <= 0:
                del self.items[item.name]
            if message is True:
                print(f"Removed {item.name} from Inventory.")
        else:
            if message is True:
                print(f"Error, {item.name} not in Inventory.")

    def display_inventory(self, player):
        print(f"||| Inventory of {player.name} |||")
        if not self.items:
            print(f"\nInventory of {player.name} is empty!")
            prompt()
            return
        for item in self.items.values():
            print("________________________________")

            if item.item_type is 'Weapon':
                print(f"[ x{item.quantity} {item.name} ] (+{item.attack} Attack)")
            if item.item_type is 'Armour':
                print(f"[ x{item.quantity} {item.name} ] (+{item.armour} Armour)")
            if item.item_type is 'Health_Potion':
                print(f"[ x{item.quantity} {item.name} ] (+{item.heal_value} Health)")
            print(f"Sell value: {item.sell_value} Gold")
        print("""
 _____________________
| [ 1 ] Equip Weapon  |
| [ 2 ] Equip Armour  |
|                     |
| [ Q ] Go back       |
|_____________________|
        """)
        answer = prompt(">> ", 'Q', 'q', '1', '2')
        if answer is 'q':
            return

        if answer is '1':
            clear_screen()
            weapons = []
            index = 1
            for item in self.items.values():
                if item.item_type is 'Weapon':
                    weapons.append(item)
            print("||| Weapons in Inventory |||")

            for item in weapons:
                print("________________________________")
                print(f"[ {index} ] {item.name} (+{item.attack} Attack)")
                index += 1
            equip_options = ('q', 'Q')
            for item_option in range(index):
                equip_options += (str(item_option),)
            print(f"\n[ 1-{index-1} Equip Weapon")
            print("[ Q ] Go back")
            answer = prompt("\n>> ", *equip_options)
            if answer is 'q' or answer is 'Q':
                return
            else:
                try:
                    pos = int(answer) - 1
                except TypeError:
                    return
                try:
                    self.equip_item(weapons[pos])
                except IndexError:
                    print("Item not found.")
                prompt()

        if answer is '2':
            clear_screen()
            armours = []
            index = 1
            for item in self.items.values():
                if item.item_type is 'Armour':
                    armours.append(item)
            print("||| Armours in Inventory |||")
            for item in armours:
                print("________________________________")
                print(f"[ {index} ] {item.name} (+{item.armour} Armour)")
                index += 1
            equip_options = ('q', 'Q')
            for item_option in range(index):
                equip_options += (str(item_option),)
            print(f"\n[ 1-{index-1} Equip Armour")
            print("[ Q ] Go back")
            answer = prompt("\n>> ", *equip_options)
            if answer is 'q' or answer is 'Q':
                return
            else:
                try:
                    pos = int(answer)-1
                except TypeError:
                    return
                try:
                    self.equip_item(armours[pos])
                except IndexError:
                    print("Item not found.")
                prompt()

    def equip_item(self, item, message=True):
        if item.name in self.items:
            pass
        else:
            if message is True:
                print("Error: You don't have that item.")
            return
        if item.item_type is not 'Armour' and item.item_type is not 'Weapon':
            if message is True:
                print(f"Error: {item.name} is not a Weapon or Armour.")
            return
        if item.item_type is 'Weapon':
            if self.weapon_equipped is False:
                self.equipment[item.name] = item
                self.remove_item(item)
                self.weapon_equipped = True
                if message is True:
                    print(f"Equipped {item.name}.")
                return
            else:
                print("You already have a Weapon equipped. Unequip it first.")
                return
        if item.item_type is 'Armour':
            if self.armour_equipped is False:
                self.equipment[item.name] = item
                self.remove_item(item)
                self.armour_equipped = True
                if message is True:
                    print(f"Equipped {item.name}.")
                return
            else:
                if message is True:
                    print("You already have an Armour equipped. Unequip it first.")
                return

    def unequip_item(self, item, message=True):
        if item.name in self.equipment:
            del self.equipment[item.name]
            if message is True:
                print(f"Unequipped {item.name}.")
                self.add_item(item)
            if item.item_type is 'Armour':
                self.armour_equipped = False
            if item.item_type is 'Weapon':
                self.weapon_equipped = False
            if message is False:
                self.add_item(item, message=False)
        else:
            if message is True:
                print(f"Error, {item.name} not in Equipment.")

    def display_equipment(self, player):
        print(f"||| Equipment of {player.name} |||")
        if not self.equipment:
            print(f"{player.name} has no items equipped!")
            prompt()
            return
        index = 1
        for item in self.equipment.values():
            print("________________________________")
            if item.item_type is 'Weapon':
                print(f"[ {index} ] {item.name} (+{item.attack} Attack)")
            if item.item_type is 'Armour':
                print(f"[ {index} ] {item.name} (+{item.armour} Armour)")
            print(f"Sell value: {item.sell_value} Gold")
            index += 1
        print("""
________________________
| [ 1 ] Unequip Weapon  |
| [ 2 ] Unequip Armour  |
|                       |
| [ Q ] Go back         |
|_______________________|
        """)
        answer = prompt("\n\n>> ", 'Q', 'q', '1', '2')
        if answer is 'q' or answer is 'Q':
            return
        if answer is '1':
            for item in self.equipment.values():
                if item.item_type is 'Weapon':
                    self.unequip_item(item)
                    prompt()
                    return
        elif answer is '2':
            for item in self.equipment.values():
                if item.item_type is 'Armour':
                    self.unequip_item(item)
                    prompt()
                    return


iron_sword = Item(name='Iron Sword', id=1, attack=5, buy_value=7, sell_value=3, item_type="Weapon")
steel_sword = Item(name='Steel Sword', id=2, attack=9, buy_value=12, sell_value=6, item_type="Weapon")
crimson_sword = Item(name='Crimson Sword', id=3, attack=14, buy_value=0, sell_value=0, item_type="Weapon")
steel_armour = Item(name='Steel Armour', id=4, armour=4, buy_value=8, sell_value=3, item_type="Armour")

item_list = [
    iron_sword,
    steel_sword,
    crimson_sword,
    steel_armour
]

inv = Inventory()
