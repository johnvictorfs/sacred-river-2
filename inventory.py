import configparser

# Local
from prompt import prompt
from clear import clear_screen


class Item:

    def __init__(self, name, attack=0, armour=0, buy_value=0, sell_value=0, heal_value=0, item_type='', quantity=0):
        """
        Item type can be: "Weapon", "Armour", "Health_Potion"

        :param name: str
        :param attack: int
        :param armour: int
        :param buy_value: int
        :param sell_value: int
        :param heal_value: int
        :param item_type: str
        """
        self.name = name
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
        print(f"--- Displaying Inventory of {player.name} ---")
        if not self.items:
            print(f"Inventory of {player.name} is empty!")
            prompt()
            return
        for item in self.items.values():
            print(f"- x{item.quantity} {item.name} - ")
            if item.item_type is 'Weapon':
                print(f"+{item.attack} Attack")
            if item.item_type is 'Armour':
                print(f"+{item.armour} Defence")
            if item.item_type is 'Health_Potion':
                print(f"+{item.health_value} Heal")
            print(f"Sell value: {item.sell_value} Gold")
            print("--------\n")
        print("1- Equip Armour")
        print("2- Equip Weapon")
        print("Q- Go back")
        answer = prompt("\n\n>> ", 'q', '1', '2')
        if answer is 'q':
            return
        if answer is '1':
            clear_screen()
            armours = []
            entry = 1
            for item in self.items.values():
                if item.item_type is 'Armour':
                    armours.append(item)
            print("--- Armours in Inventory ---")
            for item in armours:
                print(f"-{entry}: {item.name}")
                print(f"+{item.armour} Armour")
                print("--------\n")
                entry += 1
            print("- Which Armour do you want to Equip? (Q to go Back)-")
            prompt("\n\n>> ", 'Q', 'q', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
            if answer.lower() is 'q':
                return
            else:
                try:
                    pos = int(answer)-1
                    self.equip_item(armours[pos])
                except IndexError:
                    print("Item not found.")
                    prompt()
                    return

        if answer is '2':
            clear_screen()
            weapons = []
            entry = 1
            for item in self.items.values():
                if item.item_type is 'Weapon':
                    weapons.append(item)
            print("--- Weapons in Inventory ---")
            for item in weapons:
                print(f"-{entry}: {item.name}")
                print(f"+{item.attack} Attack")
                print("--------\n")
                entry += 1
            print("- Which Weapon do you want to Equip? (Q to go Back)-")
            prompt("\n\n>> ", 'q', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
            if answer is 'q':
                return
            else:
                try:
                    pos = int(answer)-1
                    self.equip_item(weapons[pos])
                except IndexError:
                    print("Item not found.")
                    prompt()
                    return

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
            self.add_item(item)
            if message is True:
                print(f"Unequipped {item.name} and added it to Inventory.")
        else:
            if message is True:
                print(f"Error, {item.name} not in Equipment.")

    def display_equipment(self, player):
        print(f"--- Displaying Equipment of {player.name} ---")
        entry = 0
        if not self.equipment:
            print(f"{player.name} has no items equipped!")
            prompt()
            return
        for item in self.equipment.values():
            entry += 1
            print(f"- Item {entry} {item.name} - ")
            if item.item_type is 'Weapon':
                print(f"+{item.attack} Attack")
            if item.item_type is 'Armour':
                print(f"+{item.armour} Defence")
            print(f"Sell value: {item.sell_value} Gold")
            print("--------\n")
        answer = prompt("< Type '1' to unequip Weapon or '2' to unequip Armour, type 'Q' to go back. >", 'q', '1', '2')
        if answer is '1':
            for item in self.equipment.values():
                if item.item_type is 'Weapon':
                    self.unequip_item(item)
        elif answer is '2':
            for item in self.equipment.values():
                if item.item_type is 'Armour':
                    self.unequip_item(item)

    def save_inventory(self):
        """
        CURRENTLY NOT WORKING
        :return:
        """
        config = configparser.ConfigParser()
        config['USER_INVENTORY'] = {}
        config['USER_EQUIPMENT'] = {}
        for item in self.items.values():
            config['USER_INVENTORY'][item.name] = item.quantity

        for item in self.equipment.values():
            config['USER_EQUIPMENT'][item.name] = item.item_type

        with open('inventory.ini', 'w') as config_file:
            config.write(config_file)


iron_sword = Item(name='Iron Sword', attack=5, buy_value=7, sell_value=3, item_type="Weapon")
steel_sword = Item(name='Steel Sword', attack=9, buy_value=12, sell_value=6, item_type="Weapon")

crimson_sword = Item(name='Crimson Sword', attack=14, buy_value=0, sell_value=0, item_type="Weapon")

steel_armour = Item(name='Steel Armour', armour=4, buy_value=8, sell_value=3, item_type="Armour")


item_list = [
    iron_sword,
    steel_sword,

    crimson_sword,

    steel_armour
]
