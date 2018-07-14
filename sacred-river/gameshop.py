# Local
import inventory
from clear import clear_screen
from prompt import prompt
from usersave import player

shop_entries = [
    inventory.iron_sword,
    inventory.steel_sword,
    inventory.steel_armour,
    inventory.health_potion
]


def buy_item(item):
    if player.gold >= item.buy_value:
        player.gold -= item.buy_value
        print(f"{player.name} bought {item.name} for {item.buy_value} gold.")
        print(f"{player.name} Gold: {player.gold}")
        inventory.inv.add_item(item)
        prompt()
        display()
    else:
        print("Hey, you don't have enough money to buy that!")
        prompt()
        display()


def sell_item(item):
    if item.name in inventory.inv.items:
        inventory.inv.remove_item(item)
        player.gold += item.sell_value
        print(f"{player.name} sold {item.name} for {item.buy_value} gold.")
        print(f"{player.name} Gold: {player.gold}")
        prompt()
    else:
        print("Hey, you don't have that item in your inventory.")
        prompt()


def display():
    clear_screen()
    print("||| Shop |||")
    index = 1
    for item in shop_entries:
        print("________________________________")
        if item.item_type is 'Armour':
            print(f"[ {index} ] {item.name} (+{item.armour} Armour)")
            print(f"Cost: {item.buy_value}")
        if item.item_type is 'Weapon':
            print(f"[ {index} ] {item.name} (+{item.attack} Attack)")
            print(f"Cost: {item.buy_value}")
        if item.item_type is 'Health_Potion':
            print(f"[ {index} ] {item.name} (+{item.heal_value} Health)")
            print(f"Cost: {item.buy_value}")
        index += 1
    print(f"\nYour Gold: [ {player.gold} ]")
    print(f"\n[ 1-{index-1} ] Buy Item ")
    print("[ S ] Sell items ")
    print("[ Q ] Go Back")
    options_tuple = ('q', 'Q', 's', 'S')
    for item_option in range(index):
        options_tuple += (str(item_option),)
    answer = prompt("\n>> ", *options_tuple)
    if answer is 'q' or answer is 'Q':
        return
    if answer is 's' or answer is 'S':
        if not inventory.inv.items.values():
            print("You don't have any items to sell.")
            prompt()
            return
        inventory_items_list = []
        index = 1
        for item in inventory.inv.items.values():
            inventory_items_list.append(item)
            print("________________________________")
            if item.item_type is 'Armour':
                print(f"[ {index} ] {item.name} (+{item.armour} Armour)")
                print(f"Sell Value: {item.sell_value}")
            if item.item_type is 'Weapon':
                print(f"[ {index} ] {item.name} (+{item.attack} Attack)")
                print(f"Sell Value: {item.sell_value}")
            if item.item_type is 'Health_Potion':
                print(f"[ {index} ] {item.name} (+{item.heal_value} Health)")
                print(f"Sell Value: {item.sell_value}")
            index += 1
        print(f"\nYour Gold: {player.gold}")
        print(f"\n[ 1-{index-1} ] Sell Item")
        print("[ Q ] Go back")
        options_tuple = ('q', 'Q')
        for item_option in range(index):
            options_tuple += (str(item_option),)
        answer = prompt("\n>> ", *options_tuple)
        if answer is 'q' or answer is 'Q':
            return
        try:
            pos = int(answer) - 1
            sell_item(inventory_items_list[pos])
            return
        except IndexError or TypeError:
            print("Item not found.")
            prompt()
            return
    try:
        pos = int(answer) - 1
        buy_item(shop_entries[pos])
        return
    except IndexError or TypeError:
        print("Item not found.")
        prompt()
        return
