# Local
import inventory
from clear import clear_screen
from prompt import prompt
from userstats import player

entries = [
    inventory.iron_sword,
    inventory.steel_sword,

    inventory.steel_armour
]

inv = inventory.Inventory()


def buy_item(item):
    if player.gold >= item.buy_value:
        player.gold -= item.buy_value
        print(f"{player.name} bought {item.name} for {item.buy_value} gold.")
        print(f"{player.name} Gold: {player.gold}")
        prompt()
    else:
        print("Hey, you don't have enough money to buy that!")
        prompt()
        return False, None
    return True, item


def sell_item(item):
    if item in inv.items:
        inv.remove_item(item)
        player.gold += item.sell_value
        print(f"{player.name} sold {item.name} for {item.buy_value} gold.")
        print(f"{player.name} Gold: {player.gold}")
        prompt()
    else:
        print("Hey, you don't have that item in your inventory.")
        prompt()


def display():
    clear_screen()
    print("--- Game Shop ---")
    print(f"Current Gold: {player.gold}")
    entry = 1
    for item in entries:
        print("---")
        print(f"Item {entry}: {item.name}")
        print(f"Cost: {item.buy_value}")
        if item.item_type is 'Armour':
            print(f"Defence bonus: {item.armour}")
        if item.item_type is 'Weapon':
            print(f"Attack bonus: {item.attack}")
        print("")
        print('\n')
        entry += 1
    answer = prompt("< Type the number of the item you wish to buy or 'Q' to go back >",
                    'q', 'Q', '1', '2', '3', '4', '5')
    if answer.lower() == 'q':
        return
    try:
        bought, item = buy_item(entries[int(answer)-1])
        if bought is True:
            return item
    except IndexError:
        print("Item not found.")
        prompt()