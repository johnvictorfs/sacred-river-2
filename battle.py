import random

# Local
from prompt import prompt
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
----- {player.name} X {npc.name} -----

- {player.name} HP: {player.health}
- {player.name} Attack: {player.attack} + {weapon_attack} from Weapon ({effective_player_attack})
- {player.name} Defence: {player.defence} + {armour_defence} from Armour ({effective_player_defence})
---------------------------------
- {npc.name} HP: {npc.health} 
- {npc.name} Attack: {npc.attack}
- {npc.name} Defence: {npc.defence}
-----
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
----- {player.name} X {npc.name} -----
{player.name} hit {player_hit}.
{npc.name} hit {npc_hit}.

- {player.name} HP: {player.health}
- {npc.name} HP: {npc.health} 
-----

    """)
        prompt()

        if player.health <= 0:
            player.death()
        if npc.health <= 0:
            break
    gold_reward = random.randint(0, npc.gold_drops)
    roll_special = random.randint(0, npc.special_drop_rate)
    special_reward = "None"
    if npc.special_drop_rate == roll_special:
        special_reward = npc.special_drop

    print(f"- {player.name} beat {npc.name} successfully and won -")
    print(f"HP: {player.health}")
    print("- Rewards -")
    print(f"- Gold: {gold_reward}")
    try:
        print(f"- Other: {special_reward.name}")
        inventory.inv.add_item(npc.special_drop)
    except AttributeError:
        print("- Other: None")
        pass
    player.gold += gold_reward
    prompt()

