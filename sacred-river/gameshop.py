# Local
import inventory
from clear import clear_screen
from prompt import prompt
from usersave import player

# Add here items that will be available for buying
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
    else:
        print("Hey, you don't have enough money to buy that!")


def sell_item(item, message=True):
    if item.name in inventory.inv.items:
        inventory.inv.remove_item(item)
        player.gold += item.sell_value
        if message is True:
            print(f"{player.name} sold {item.name} for {item.sell_value} gold.")
            print(f"{player.name} Gold: {player.gold}")
    else:
        if message is True:
            print("Hey, you don't have that item in your inventory.")


def display():
    shop_list = {}
    clear_screen()
    print("||| Shop |||")
    index = 0
    for item in shop_entries:
        index += 1
        shop_list[index] = item
        print("________________________________")
        if item.item_type is 'Armour':
            print(f"[ {index} ] {item.name} (+{item.armour} Armour)")
        if item.item_type is 'Weapon':
            print(f"[ {index} ] {item.name} (+{item.attack} Attack)")
        if item.item_type is 'Health_Potion':
            print(f"[ {index} ] {item.name} (+{item.heal_value} Health)")
        print(f"Cost: {item.buy_value}")
    print(f"""
Your Gold: [ {player.gold} ]

[ 1-{index} ] Buy Item
[ S ] Sell items
[ Q ] Go Back""")
    options = ('q', 'Q', 's', 'S')
    for item in range(index + 1):
        options += (str(item),)
    answer = prompt("\n>> ", *options)
    if answer is 'q' or answer is 'Q':
        return
    elif answer is 's' or answer is 'S':
        sell_inventory_items()
        display()
    else:
        try:
            buy_item(shop_list[int(answer)])
            prompt()
            display()
        except (IndexError, TypeError, KeyError, ValueError):
            print("Item not found.")
            prompt()
            display()
            return


def sell_inventory_items():
    if not inventory.inv.items.values():
        print("You don't have any items to sell.")
        prompt()
        return
    inventory_list = {}
    index = 0
    for item in inventory.inv.items.values():
        index += 1
        inventory_list[index] = item
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
    print(f"\nYour Gold: {player.gold}")
    print(f"\n[ 1-{index} ] Sell Item")
    print("[ Q ] Go back")
    answer = prompt("\n>> ")
    if answer is 'q' or answer is 'Q':
        display()
        return
    else:
        try:
            sell_item(inventory_list[int(answer)])
            prompt()
            sell_inventory_items()
        except (IndexError, TypeError, KeyError, ValueError):
            print("Item not found.")
            prompt()
            sell_inventory_items()
