# Local
import inventory
from clear import clear_screen
from prompt import prompt
from usersave import player

shop_entries = [
    inventory.iron_sword,
    inventory.steel_sword,
    inventory.steel_armour
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
    if item in inventory.inv.items:
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
        index += 1
    print(f"\nYour Gold: [ {player.gold} ]")
    print("\n[ Type the number of the item you wish to buy or 'Q' to go back ]")
    answer = prompt("\n>> ",
                    'q', 'Q', '1', '2', '3', '4', '5')
    if answer is 'q' or answer is 'Q':
        return
    try:
        buy_item(shop_entries[int(answer) - 1])
    except IndexError:
        print("Item not found.")
        prompt()
