import random

# Local
from prompt import prompt
from clear import clear_screen
import inventory


def battle(player, npc):
    """
    :param player: Monster
    :param npc: Player
    :return: None
    """
    for item in inventory.inv.equipment.values():
        if item.item_type == 'Weapon':
            weapon_attack = item.attack
            break
    else:
        weapon_attack = 0
    for item in inventory.inv.equipment.values():
        if item.item_type == 'Armour':
            armour_defence = item.armour
            break
    else:
        armour_defence = 0
    effective_player_defence = player.defence + armour_defence
    effective_player_attack = player.attack + weapon_attack
    npc.health = npc.max_health
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
__________________________________________""")
        if player.health <= 0:
            player.death()
        if npc.health <= 0:
            break
        print(f"""
[ Enter ] Attack
[   1   ] Attack
[   2   ] Drink HP Potion
[   Q   ] Run Away!

Current Run chance: {player.luck} roll(s) at 1/5 Chance.""")
        answer = prompt("\n>> ", '', '1', '2', 'q', 'Q')
        if answer is '1':
            pass
        elif answer is '2':
            for item in inventory.inv.items.values():
                if item.item_type is 'Health_Potion':
                    inventory.inv.drink_potion(item, player)
            else:
                print("You don't have any Health Potions.")
                prompt()
        if answer is 'q' or answer is 'Q':
            for number in range(player.luck):
                if random.randint(0, 5) is 5:
                    clear_screen()
                    print("You ran away successfully. What a coward!")
                    prompt()
                    return
            clear_screen()
            print("You couldn't get away! Tough luck.")
            prompt()

    gold_reward = random.randint(0, npc.gold_drops)
    print(f"""
[ {player.name} beat {npc.name} successfully. ]

[ HP: {player.health}/{player.max_health} ]
________________________________________________
[      REWARDS      ]

[ Gold: {gold_reward} ]
    """)
    for number in range(player.luck):
        if random.randint(0, npc.extra_drop_rate) == npc.extra_drop_rate:
            try:
                print(f"[ Other: {npc.extra_drop.name} ]")
                inventory.inv.add_item(npc.extra_drop)
                break
            except AttributeError:
                pass
    else:
        print("[ Other: None ]")
    player.level_up(skill='attack', chance=7, increase=5)
    player.level_up(skill='defence', chance=25, increase=3)
    player.level_up(skill='health', chance=15, increase=5)
    player.level_up(skill='luck', chance=5, increase=2)

    player.gold += gold_reward
    prompt()
