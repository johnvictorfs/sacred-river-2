# Local
from clear import clear_screen
import inventory


class Monster:

    def __init__(self, name, attack, defence, health, max_health=0, gold_drops=(), extra_drop=None, extra_drop_rate=0):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.health = health
        self.max_health = max_health
        self.max_health = health
        self.gold_drops = gold_drops
        self.extra_drop = extra_drop
        self.extra_drop_rate = extra_drop_rate

    def display(self):
        clear_screen()
        print(f"""
_________________________________________
||| Displaying NPC info of {self.name} |||
- Attack: {self.attack}
- Defence: {self.defence}
- Health: {self.health}/{self.max_health}
- Gold Drops: 0-{self.gold_drops}
- Extra Drop: {self.extra_drop} (Rate 1/{self.extra_drop_rate})
_________________________________________
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

crimson_skeleton_1 = Monster(name="Crimson Skeleton",
                             attack=18,
                             defence=11,
                             health=30,
                             gold_drops=15,
                             extra_drop=inventory.crimson_sword,
                             extra_drop_rate=1)

crimson_mage_1 = Monster(name="Crimson Mage",
                         attack=17,
                         defence=8,
                         health=15,
                         gold_drops=10,
                         extra_drop=inventory.crimson_staff,
                         extra_drop_rate=2)

low_level_monsters = [
    goblin_1,
    goblin_2,
    goblin_3,

    spider_1,
    spider_2,
    spider_3,

    crimson_skeleton_1,
    crimson_mage_1
]
