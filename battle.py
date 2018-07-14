import random

# Local
from prompt import prompt
from clear import clear_screen
import inventory


def battle(player, npc):
    """
    Returns a tuple of (player.health, npc.health)
    :param player: Monster
    :param npc: Player
    :return: int
    """
    weapon_attack = 0
    for item in inventory.inv.equipment.values():
        if item.item_type == 'Weapon':
            weapon_attack = item.attack
    armour_defence = 0
    for item in inventory.inv.equipment.values():
        if item.item_type == 'Armour':
            armour_defence = item.armour
    effective_player_defence = player.defence + armour_defence
    effective_player_attack = player.attack + weapon_attack
    print(f"""
______ {player.name} Vs {npc.name} ______

- {player.name} HP: {player.health}/{player.max_health}
- {player.name} Attack: {player.attack} + {weapon_attack} from Weapon ({effective_player_attack})
- {player.name} Defence: {player.defence} + {armour_defence} from Armour ({effective_player_defence})
-----------------------------------------
- {npc.name} HP: {npc.health}/{npc.max_health}
- {npc.name} Attack: {npc.attack}
- {npc.name} Defence: {npc.defence}
__________________________________________
    """)
    prompt()

    while True:
        player_hit = random.randint(0, effective_player_attack) - random.randint(0, npc.defence)
        npc_hit = random.randint(0, npc.attack) - random.randint(0, effective_player_defence)
        if player_hit < 0:
            player_hit = 0
        if npc_hit < 0:
            npc_hit = 0
        player.health -= npc_hit
        npc.health -= player_hit

        print(f"""
______ {player.name} Vs {npc.name} ______
{player.name} hit {player_hit}.
{npc.name} hit {npc_hit}.
-----------------------------------------
- {player.name} HP: {player.health}/{player.max_health}
- {npc.name} HP: {npc.health}/{npc.max_health}
__________________________________________

    """)
        if player.health <= 0:
            player.death()
        if npc.health <= 0:
            break
        print("[ 1/Enter ] Attack")
        print("[ 2 ] Drink HP Potion")
        print(f"[ Q ] Run Away! ({player.luck} roll(s) at a 1/5 Chance)")
        answer = prompt("\n>> ")
        if answer is '1':
            pass
        elif answer is '2':
            found = False
            for item in inventory.inv.items.values():
                if item.item_type is 'Health_Potion':
                    inventory.inv.drink_potion(item, player)
                    found = True
                    break
            if found is False:
                print("You don't have any Health Potions.")
                prompt()
        if answer is 'q' or answer is 'Q':
            for number in range(player.luck):
                run_away = random.randint(0, 5)
                if run_away is 5:
                    clear_screen()
                    print("You ran away successfully. What a coward!")
                    prompt()
                    return
            clear_screen()
            print("You couldn't get away! Tough luck.")
            prompt()

    gold_reward = random.randint(0, npc.gold_drops)
    extra_reward = "None"
    for number in range(player.luck):
        roll_special = random.randint(0, npc.extra_drop_rate)
        if npc.extra_drop_rate == roll_special:
            extra_reward = npc.extra_drop

    print(f"- {player.name} beat {npc.name} successfully and won -")
    print(f"HP: {player.health}/{player.max_health}")
    print("- Rewards -")
    print(f"- Gold: {gold_reward}")

    roll_level_hp = random.randint(0, 50)
    if roll_level_hp is 25:
        old_health = player.max_health
        player.max_health += random.randint(5, 15)
        player.health = player.max_health
        print(f"\n* LEVEL UP: Your Max health is now {player.max_health} (from {old_health}).")
        print("- Your HP has also been healed to Maximum. -")
    roll_level_luck = random.randint(0, 50)
    if roll_level_luck is 15:
        old_luck = player.luck
        player.luck += random.randint(1, 3)
        print(f"\n* LEVEL UP: Your Luck is now {player.luck} (from {old_luck}).")
    roll_level_attack = random.randint(0, 50)
    if roll_level_attack is 10:
        old_attack = player.attack
        player.attack += random.randint(1, 4)
        print(f"\n* LEVEL UP: Your Attack is now {player.attack} (from {old_attack}).")
    roll_level_defence = random.randint(0, 50)
    if roll_level_defence is 15:
        old_defence = player.defence
        player.defence += random.randint(2, 6)
        print(f"\n* LEVEL UP: Your Defence is now {player.defence} (from {old_defence}).")
    try:
        print(f"- Other: {extra_reward.name}")
        inventory.inv.add_item(npc.special_drop)
    except AttributeError:
        print("- Other: None")
        pass
    player.gold += gold_reward
    prompt()

