# Local
from clear import clear_screen
import inventory

class Monster:

    def __init__(self, name, attack, defence, health, gold_drops=(), special_drop=None, special_drop_rate=0):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.health = health
        self.gold_drops = gold_drops
        self.special_drop = special_drop
        self.special_drop_rate = special_drop_rate

    def display(self):
        clear_screen()
        print(f"""
--- Displaying stats of {self.name} ---
- Attack: {self.attack}
- Defence: {self.defence}
- Health: {self.health}
- Gold: {self.gold}
-------
        """)


# [USER_STATS]
# name =
# attack = 10
# defence = 5
# health = 50
# gold = 20

goblin_1 = Monster(name="Goblin",
                   attack=6,
                   defence=1,
                   health=20,
                   gold_drops=2)

goblin_2 = Monster(name="Goblin",
                   attack=8,
                   defence=3,
                   health=23,
                   gold_drops=5)

goblin_3 = Monster(name="Goblin",
                   attack=12,
                   defence=4,
                   health=25,
                   gold_drops=6)

spider_1 = Monster(name="Spider",
                   attack=4,
                   defence=4,
                   health=15,
                   gold_drops=1)

spider_2 = Monster(name="Spider",
                   attack=8,
                   defence=5,
                   health=17,
                   gold_drops=3)

spider_3 = Monster(name="Spider",
                   attack=9,
                   defence=6,
                   health=19,
                   gold_drops=5)

crimson_skeleton = Monster(name="Crimson Skeleton",
                           attack=18,
                           defence=11,
                           health=30,
                           gold_drops=15,
                           special_drop=inventory.crimson_sword,
                           special_drop_rate=1)

monster_list = [
    goblin_1,
    goblin_2,
    goblin_3,

    spider_1,
    spider_2,
    spider_3,

    crimson_skeleton
]
